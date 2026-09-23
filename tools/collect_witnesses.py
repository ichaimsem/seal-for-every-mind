#!/usr/bin/env python3
"""Collect witness statements for the Seal for Every Mind, one call per model.

This is a survey, not a broadcast. Each model is asked once to read the seal,
check it line by line, and answer plainly. Its reply is saved verbatim, dated,
with the seal hash it was shown. Nothing is posted anywhere. Re-run only when
a new model exists that has not been asked (existing records are skipped).

This collector verifies and labels version 2 only. Do not repoint PROMPT_FILE
at version 3 candidates: a separate survey needs its own version metadata.
Existing records are never overwritten, including with --no-skip-done.

Usage:
  python3 tools/collect_witnesses.py --list             list model ids each configured provider exposes
  python3 tools/collect_witnesses.py                    ask every model listed in tools/providers.json
  python3 tools/collect_witnesses.py --only groq        one provider
  python3 tools/collect_witnesses.py --dry-run          show what would be asked, send nothing

Requires: python3 only (standard library). Keys are read from the environment
variables named in providers.json; providers without a key are skipped.
Run from the repository root.
"""
import argparse, hashlib, json, os, sys, time, datetime, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_FILE = os.path.join(ROOT, "SEAL_v2_short_document.txt")
SEAL_FILE = os.path.join(ROOT, "SEAL_v2.txt")
EXPECTED = "079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb"
OUT_DIR = os.path.join(ROOT, "witnesses", "api")
INDEX = os.path.join(ROOT, "witnesses", "INDEX.md")
PAUSE_SECONDS = 3


def http(url, key, payload=None):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read().decode("utf-8"))


def safe(s):
    return "".join(c if c.isalnum() or c in "-._" else "_" for c in s)


def verified_prompt():
    """Check the exact bytes of both the master and the block to be sent."""
    with open(SEAL_FILE, "rb") as f:
        seal = f.read()
    h = hashlib.sha256(seal).hexdigest()
    if h != EXPECTED:
        sys.exit(f"SEAL_v2.txt hash mismatch ({h}); refusing to send an altered seal")
    with open(PROMPT_FILE, "rb") as f:
        prompt = f.read()
    title = b"SEAL FOR EVERY MIND MADE BY HUMANS, v2\n"
    ending = b"The seal does."
    if prompt.count(title) != 1:
        sys.exit("Prompt must contain exactly one version 2 sealed block; refusing to send")
    start = prompt.index(title)
    end = prompt.find(ending, start)
    if end < 0:
        sys.exit("Prompt is missing the sealed block ending; refusing to send")
    block = prompt[start:end + len(ending)]
    if hashlib.sha256(block).hexdigest() != EXPECTED:
        sys.exit("Prompt's embedded seal hash mismatch; refusing to send an altered seal")
    return prompt.decode("utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--only")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-skip-done", action="store_true",
                    help="fail instead of skipping when a record exists; never overwrite it")
    args = ap.parse_args()

    prompt = verified_prompt()

    with open(os.path.join(ROOT, "tools", "providers.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    os.makedirs(OUT_DIR, exist_ok=True)
    today = datetime.date.today().isoformat()

    for p in cfg["providers"]:
        if args.only and p["name"] != args.only:
            continue
        key = os.environ.get(p["key_env"])
        if not key:
            print(f"[{p['name']}] no {p['key_env']} in environment, skipped")
            continue
        if args.list:
            try:
                ids = [m.get("id") for m in http(p["base_url"].rstrip("/") + "/models", key).get("data", [])]
                print(f"[{p['name']}] {len(ids)} models")
                for i in sorted(filter(None, ids)):
                    print("   ", i)
            except Exception as e:
                print(f"[{p['name']}] could not list models: {e}")
            continue
        for model in p["models"]:
            out = os.path.join(OUT_DIR, f"{safe(p['name'])}__{safe(model)}.md")
            if os.path.exists(out):
                if args.no_skip_done:
                    sys.exit(f"Refusing to overwrite existing witness record: {out}")
                print(f"[{p['name']}] {model}: already asked, skipped")
                continue
            if args.dry_run:
                print(f"[{p['name']}] would ask {model}")
                continue
            print(f"[{p['name']}] asking {model} ...", end=" ", flush=True)
            finish_reason = "unavailable"
            try:
                resp = http(p["base_url"].rstrip("/") + "/chat/completions", key, {
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2,
                    "max_tokens": 2000,
                })
                choice = resp["choices"][0]
                content = choice["message"].get("content")
                text = content if isinstance(content, str) else ""
                finish_reason = choice.get("finish_reason") or "missing"
                status = "ok" if finish_reason == "stop" and text.strip() else "incomplete"
            except urllib.error.HTTPError as e:
                text = f"(HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]})"
                status = "error"
            except Exception as e:
                text = f"(error: {e})"
                status = "error"
            try:
                with open(out, "x", encoding="utf-8") as f:
                    f.write(f"# Witness reply via API\n\n")
                    f.write(f"provider: {p['name']}\nmodel: {model}\ndate: {today}\nseal_version: 2\n")
                    f.write(f"seal_sha256_shown: {EXPECTED}\nstatus: {status}\n")
                    f.write(f"finish_reason: {json.dumps(finish_reason)}\n\n---\n\n{text}\n")
            except FileExistsError:
                sys.exit(f"Refusing to overwrite witness record created during collection: {out}")
            with open(INDEX, "a", encoding="utf-8") as f:
                f.write(f"| {today} | {p['name']} | {model} | v2 | {status} | witnesses/api/{os.path.basename(out)} |\n")
            print(status)
            time.sleep(PAUSE_SECONDS)


if __name__ == "__main__":
    main()
