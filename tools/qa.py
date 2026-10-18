#!/usr/bin/env python3
"""One-command QA for this repository. Run from the repository root.

  python3 tools/qa.py              offline checks
  python3 tools/qa.py --online     also load every external link (Sefaria, GitHub, archive)
  python3 tools/qa.py --fix-hashes rewrite the per-file lines in HASHES.txt, then check

FAIL means something is broken and must be fixed before merging.
WARN means something is out of date or needs a human look; it does not block.

Checks:
  seal        verify.py: every sealed block and every embedded copy matches its hash
  llms-full   llms-full.txt matches what tools/build_llms_full.py would build
  hashes      HASHES.txt lists every tracked file with its current SHA-256
  json        ai-index.json parses, and its loop has as many stations as LOOP.md
  index       foundation wording, station content and curriculum sources agree
  inventory   README lists every tracked file exactly once
  witnesses   witnesses/INDEX.md agrees with the record it points at, field by field
  links       every relative link in the Markdown files points at a file that exists
  name        the Divine Name is not spelled out in full anywhere (write ה׳)
  dashes      no em dashes outside the verbatim witness records
  online      (--online) every external URL answers 200 (witness records and API
              endpoints in tools/providers.json are not checked)
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

results = []  # (status, check, detail)


def report(status, check, detail=""):
    results.append((status, check, detail))


def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True, check=True).stdout
    return sorted(f for f in out.split("\0") if f)


def check_seal():
    r = subprocess.run([sys.executable, "verify.py"], capture_output=True, text=True)
    last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()
    report("OK" if r.returncode == 0 else "FAIL", "seal", last)


def check_llms_full():
    r = subprocess.run([sys.executable, "tools/build_llms_full.py", "--check"], capture_output=True, text=True)
    report("OK" if r.returncode == 0 else "FAIL", "llms-full", r.stdout.strip() or r.stderr.strip())


HASH_LINE = re.compile(r"^  ([0-9a-f]{64})  ([^\n]+)$", re.M)


def per_file_section(text):
    start = text.index("SHA-256 of each file in the repository")
    end = text.index("\nVerify with: python3 verify.py")
    return start, end


def fix_hashes(files):
    text = Path("HASHES.txt").read_text(encoding="utf-8")
    start, end = per_file_section(text)
    header = text[start:].split("\n", 1)[0] + "\n"
    body = "".join(
        f"  {hashlib.sha256(Path(f).read_bytes()).hexdigest()}  {f}\n" for f in files if f != "HASHES.txt"
    )
    Path("HASHES.txt").write_text(text[:start] + header + body + text[end:], encoding="utf-8")


def check_hashes(files):
    text = Path("HASHES.txt").read_text(encoding="utf-8")
    start, end = per_file_section(text)
    entries = HASH_LINE.findall(text[start:end])
    listed = dict((p, h) for h, p in entries)
    duplicate = len(entries) != len(listed)
    want = [f for f in files if f != "HASHES.txt"]
    missing = [f for f in want if f not in listed]
    extra = [f for f in listed if f not in want]
    stale = [f for f in want if f in listed and hashlib.sha256(Path(f).read_bytes()).hexdigest() != listed[f]]
    if missing or extra or stale or duplicate:
        report("FAIL", "hashes", f"missing {missing} extra {extra} stale {stale} duplicates {duplicate}; run python3 tools/qa.py --fix-hashes and add a dated line to the HASHES.txt narrative")
    else:
        report("OK", "hashes", f"{len(want)} files")
    for name, h in [("SEAL_v1.txt", "9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa"),
                    ("SEAL_v2.txt", "079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb")]:
        if f"  {name}  {h}" not in text:
            report("FAIL", "hashes", f"sealed-block line for {name} changed")


def check_json():
    try:
        idx = json.loads(Path("ai-index.json").read_text(encoding="utf-8"))
    except Exception as e:
        report("FAIL", "json", f"ai-index.json does not parse: {e}")
        return
    loop_md = Path("LOOP.md").read_text(encoding="utf-8")
    n_md = len(re.findall(r"^### \d+\. ", loop_md, re.M))
    n_js = len(idx.get("loop", {}).get("stations", []))
    if n_md != n_js:
        report("FAIL", "json", f"LOOP.md has {n_md} stations, ai-index.json has {n_js}")
    else:
        report("OK", "json", f"ai-index.json parses; loop has {n_js} stations in both")
    r = subprocess.run([sys.executable, "tools/sync_ai_index.py", "--check"], capture_output=True, text=True)
    report("OK" if r.returncode == 0 else "FAIL", "index", r.stdout.strip() or r.stderr.strip())


def check_inventory(files):
    text = Path("README.md").read_text(encoding="utf-8")
    section = text.split("## What is in this repository\n", 1)[1].split("\n## ", 1)[0]
    listed = [row.split("|")[1].strip() for row in section.splitlines() if row.startswith("| ")][1:]
    # A row ending in "/" stands for every tracked file under that folder, so the
    # landing page can name a folder of records instead of listing each one.
    folders = [entry for entry in listed if entry.endswith("/")]
    covered = {f for f in files if any(f.startswith(folder) for folder in folders)}
    missing = sorted(set(files) - set(listed) - covered)
    extra = sorted({entry for entry in listed if not entry.endswith("/")} - set(files)
                   | {folder for folder in folders if not any(f.startswith(folder) for f in files)})
    duplicate = len(listed) != len(set(listed))
    report("FAIL" if missing or extra or duplicate else "OK", "inventory",
           f"missing {missing}; extra {extra}; duplicates {duplicate}" if missing or extra or duplicate
           else f"README lists all {len(files)} tracked files")


def check_links(files):
    bad = []
    for f in files:
        if not f.endswith(".md") and f != "llms.txt":
            continue
        for m in re.finditer(r"\]\(([^)\s]+)\)", Path(f).read_text(encoding="utf-8")):
            t = m.group(1)
            if t.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not os.path.exists(os.path.join(os.path.dirname(f), t.split("#")[0])):
                bad.append(f"{f} -> {t}")
    report("FAIL" if bad else "OK", "links", "; ".join(bad) if bad else "all relative links resolve")


NAME = re.compile("י[֑-ׇ]*ה[֑-ׇ]*ו[֑-ׇ]*ה")


def check_name(files):
    hits = []
    for f in files:
        if f.endswith((".md", ".txt", ".json", ".py")):
            n = len(NAME.findall(Path(f).read_text(encoding="utf-8")))
            if n:
                hits.append(f"{f} ({n})")
    report("FAIL" if hits else "OK", "name", "; ".join(hits) if hits else "not spelled out anywhere")


def check_dashes(files):
    hits = [f for f in files if f.endswith((".md", ".txt")) and "WITNESSES" not in f
            and not f.startswith("witnesses/") and "—" in Path(f).read_text(encoding="utf-8")]
    report("FAIL" if hits else "OK", "dashes", "; ".join(hits) if hits else "none outside witness records")


WITNESS_FIELDS = ("provider", "model", "date", "seal_version", "seal_sha256_shown", "status")
WITNESS_COLUMNS = ("date", "provider", "model", "version", "status", "file")


def check_witnesses(files):
    """The index is a ledger, so it must agree with the record it points at.

    A record is evidence. If the index and the record disagree about what a model
    answered, the ledger is no longer trustworthy, whichever of the two is wrong.
    The columns are compared by name, not by position in the row.
    """
    index = Path("witnesses/INDEX.md")
    records = sorted(f for f in files if f.startswith("witnesses/api/") and f.endswith(".md"))
    if not index.exists():
        report("FAIL", "witnesses", "witnesses/INDEX.md is missing")
        return
    rows = [line for line in index.read_text(encoding="utf-8").splitlines()
            if line.startswith("| ") and not set(line) <= set("|- ")]
    if not rows:
        report("FAIL", "witnesses", "witnesses/INDEX.md has no rows")
        return
    header = [cell.strip() for cell in rows[0].strip().strip("|").split("|")]
    if header != list(WITNESS_COLUMNS):
        report("FAIL", "witnesses", f"witnesses/INDEX.md columns are {header}, expected {list(WITNESS_COLUMNS)}")
        return

    problems, warnings, seen, row_files = [], [], {}, []
    for row in rows[1:]:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if len(cells) != len(WITNESS_COLUMNS):
            problems.append(f"row has {len(cells)} columns, expected {len(WITNESS_COLUMNS)}: {row.strip()[:60]}")
            continue
        entry = dict(zip(WITNESS_COLUMNS, cells))
        name = entry["file"]
        row_files.append(name)
        if name in seen:
            problems.append(f"{name} is listed more than once")
            continue
        seen[name] = entry
        if not os.path.exists(name):
            problems.append(f"{name} is listed but does not exist")
            continue
        if name not in records:
            warnings.append(f"{name} is listed but is not a tracked witness record")

    for name in records:
        if name not in seen:
            problems.append(f"{name} is not listed in witnesses/INDEX.md")

    expected_seal = hashlib.sha256(Path("SEAL_v2.txt").read_bytes()).hexdigest()
    for name in records:
        entry = seen.get(name)
        if entry is None:
            continue
        text = Path(name).read_text(encoding="utf-8")
        fields = dict(re.findall(r"^(%s): *(.+)$" % "|".join(WITNESS_FIELDS), text, re.M))
        for field in WITNESS_FIELDS:
            if field not in fields:
                warnings.append(f"{name} has no {field}: line")
        # finish_reason is not required here. Two records predate the collector
        # writing it, and a record is never rewritten to add a field, so
        # demanding it would leave a warning no one is allowed to clear.
        pairs = [("provider", "provider"), ("model", "model"), ("date", "date"),
                 ("status", "status"), ("seal_version", "version")]
        for column, field in pairs:
            if field in fields and entry[column] != fields[field]:
                problems.append(f"{name}: index {column}={entry[column]!r} but record {field}={fields[field]!r}")
        if "seal_sha256_shown" in fields and fields["seal_sha256_shown"] != expected_seal:
            problems.append(f"{name}: shows seal hash {fields['seal_sha256_shown'][:16]}... "
                            f"but SEAL_v2.txt hashes to {expected_seal[:16]}...")

    ok = [f for f in records if seen.get(f, {}).get("status") == "ok"]
    errors = [f for f in records if seen.get(f, {}).get("status") == "error"]
    summary = (f"{len(records)} records, {len(ok)} with a usable reply, {len(errors)} failed at the provider")
    if problems:
        report("FAIL", "witnesses", summary + "; " + "; ".join(problems))
    elif warnings:
        report("WARN", "witnesses", summary + "; " + "; ".join(warnings))
    else:
        report("OK", "witnesses", summary + "; index agrees with every record")


def external_urls(text):
    """Read literal URLs, excluding parameterized examples and Markdown delimiters."""
    # Captured command output is historical evidence, not a list of live links.
    text = re.sub(r"(?ms)^```(?:console|text)\n.*?^```[ \t]*$", "", text)
    # verify.py accepts a raw directory base, not an independently fetchable page.
    # Exclude only its command argument; an ordinary link to that URL is checked.
    text = re.sub(r"(\bverify\.py\s+)https?://[^\s`]+", r"\1<raw-url-base>", text)
    urls = set()
    for candidate in re.findall(r"https?://[^\s)\"`\]]+", text):
        # Keep angle-bracket placeholders together so an API template is not
        # accidentally truncated into a real (and usually nonexistent) URL.
        if "<" in candidate or "$" in candidate or "USER" in candidate:
            continue
        urls.add(candidate.rstrip(".,;:'>"))
    return urls


TRANSIENT_CURL_EXITS = {6, 7, 28, 35, 52, 55, 56}
RETRY_PAUSE_SECONDS = 5

# classify curl's answer as one of:
#   "ok"            the page opened
#   "retry"         a network fault worth one more attempt
#   "unverifiable"  the page could not be opened, and that is not the link's fault
#   "broken"        the link itself is the problem
CHALLENGE = "cf-mitigated: challenge"


def curl_once(u):
    """One attempt. Returns (http_code, lowercase headers, curl return code)."""
    with tempfile.TemporaryDirectory() as d:
        headers = os.path.join(d, "headers")
        response = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-D", headers, "-L", "--max-time", "40",
             "--retry", "1", "--retry-max-time", "60", "-w", "%{http_code}", u],
            capture_output=True, text=True)
        try:
            raw = Path(headers).read_text(encoding="utf-8", errors="replace").lower()
        except OSError:
            raw = ""
        return response.stdout, raw, response.returncode


def classify(code, raw, returncode):
    """Turn one attempt into a verdict and the line to report.

    A bot challenge is not a broken link: Cloudflare answers 403 with
    cf-mitigated: challenge for pages a browser opens normally, including the
    chabad.org Mishneh Torah chapters cited here that are not on Sefaria. A
    transport error or a 5xx is a network fault, not a missing page: the same
    web.archive.org URL answered 200 and then 500 in two runs on 12 October 2026.
    Failing the build for either trains a reader to ignore a red check, which is
    worse than no check. Both are reported as unchecked, and a link is never
    reported as working when it was not opened.
    """
    if returncode in TRANSIENT_CURL_EXITS or (not returncode and code.startswith("5")):
        return "retry", f"HTTP {code}" if code else f"curl exit {returncode}"
    if not returncode and code == "200":
        return "ok", ""
    if not returncode and code in ("403", "503") and CHALLENGE in raw:
        return "unverifiable", f"{code} bot challenge, not opened"
    if returncode:
        return "broken", f"curl exit {returncode}, HTTP {code}"
    return "broken", code


def fetch_url(u):
    """Fetch one URL, giving a network fault one more attempt before believing it."""
    verdict, detail = classify(*curl_once(u))
    if verdict == "retry" or (verdict == "broken" and is_archive(u)):
        time.sleep(RETRY_PAUSE_SECONDS)
        verdict, detail = classify(*curl_once(u))
    if verdict == "ok":
        return None, False
    if verdict == "unverifiable":
        return f"{detail} {u}", True
    if verdict == "retry":
        # Still faulting after a second attempt. Not opened, and not proven dead.
        return f"{detail} after two attempts {u}", True
    if is_archive(u):
        # The Internet Archive cannot gate this build. On 12 October 2026, across
        # repeated runs on the same day, three archive.org URLs returned 200, then
        # 500, 404 and a curl transport failure, and the repository snapshot URL
        # listed in README.md returned 200 on one attempt and a transport failure on
        # the next. An answer from that host therefore says little about the page.
        # Archived copies are a bonus here, not the guarantee; the live repository is.
        return f"{detail}, archive.org answer not trusted {u}", True
    return f"{detail} {u}", False


def is_archive(u):
    return "web.archive.org" in u or "archive.org/" in u


def check_online(files, urls=None):
    """urls is injectable so the decision can be tested without the network."""
    collected = set()
    for f in files:
        # Witness records are verbatim and tools/providers.json holds API endpoints, not pages.
        if f.startswith("witnesses/") or f in ("WITNESSES.md", "tools/providers.json"):
            continue
        if f.endswith((".md", ".txt", ".json")):
            collected.update(external_urls(Path(f).read_text(encoding="utf-8")))
    if urls is None:
        urls = collected
    skip = ("web.archive.org/save", "/issues/new", "creativecommons.org")
    urls = sorted(u for u in urls if not any(s in u for s in skip) and "USER" not in u and "$" not in u)
    with ThreadPoolExecutor(max_workers=6) as pool:
        outcomes = list(pool.map(fetch_url, urls))
    bad = [p for p, _ in outcomes if p and not _]
    unchecked = [p for p, unverifiable in outcomes if p and unverifiable]
    detail = f"{len(urls)} URLs; "
    if bad:
        detail += "; ".join(bad)
        if unchecked:
            detail += "; and not opened: " + "; ".join(unchecked)
        report("FAIL", "online", detail)
    elif unchecked:
        detail += "all opened except " + "; ".join(unchecked)
        report("WARN", "online", detail)
    else:
        report("OK", "online", detail + "all 200")


def main():
    files = tracked()
    missing = [f for f in files if not os.path.isfile(f)]
    if missing:
        print("FAIL  files  tracked files missing from working tree: " + "; ".join(missing))
        print("QA FAILED")
        sys.exit(1)
    if "--fix-hashes" in sys.argv:
        fix_hashes(files)
    check_seal()
    check_llms_full()
    check_hashes(files)
    check_json()
    check_inventory(files)
    check_witnesses(files)
    check_links(files)
    check_name(files)
    check_dashes(files)
    if "--online" in sys.argv:
        check_online(files)
    width = max(len(c) for _, c, _ in results)
    for status, check, detail in results:
        print(f"{status:4}  {check:<{width}}  {detail}")
    failed = any(s == "FAIL" for s, _, _ in results)
    print("QA FAILED" if failed else "QA PASSED")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
