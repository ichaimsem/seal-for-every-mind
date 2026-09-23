#!/usr/bin/env python3
"""Keep the index's reading map aligned with its Markdown source documents.

Run with --check in QA, or without arguments to refresh derived fields.
Interpretive notes, print bibliographies and the owner's other wording remain
manually maintained. This script does not certify a source as checked.
"""
import copy
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def sources(text):
    seen = set()
    out = []
    for label, url in LINK.findall(text):
        if url not in seen:
            out.append({"cite": label, "url": url})
            seen.add(url)
    return out


def synchronize(index, foundation, loop, curriculum):
    result = copy.deepcopy(index)
    english = re.findall(r"^\d\. (.+)$", foundation.split("בעברית:")[0], re.M)
    plain = re.sub(r"<[^>]+>", "", foundation)
    hebrew = re.findall(r"^[א-ד]\. (.+)$", plain, re.M)
    if len(english) != 4 or len(hebrew) != 4 or len(result["foundation"]["statements"]) != 4:
        raise ValueError("expected exactly four English and Hebrew foundation statements")
    for n, (en, he, statement) in enumerate(zip(english, hebrew, result["foundation"]["statements"]), 1):
        statement.update(n=n, en=en, he=he)
        section = re.search(r"^## " + str(n) + r"\. [^\n]+\n(.*?)(?=^## |^---|\Z)", foundation, re.M | re.S)
        if not section:
            raise ValueError(f"foundation section {n} missing")
        metadata = {source["url"]: source for source in statement.get("sources", [])}
        statement["sources"] = [{**metadata.get(source["url"], {}), **source}
                                for source in sources(section[1])]
    result["foundation"]["source_urls"] = [s["url"] for s in sources(foundation)]

    stations = []
    for match in re.finditer(r"^### (\d+)\. ([^\n]+)\n(.*?)(?=^### |^---|\Z)", loop, re.M | re.S):
        n, question, body = match.groups()
        def field(name):
            found = re.search(r"^\*\*" + re.escape(name) + r":\*\* (.+)$", body, re.M)
            if not found:
                raise ValueError(f"station {n} missing {name}")
            return found.group(1)
        stations.append({"n": int(n), "question": question,
                         "open": sources(field("Open")), "look_for": field("Look for"),
                         "opens": field("It opens"), "next": int(n) + 1})
    if not stations or [s["n"] for s in stations] != list(range(1, len(stations) + 1)):
        raise ValueError("loop stations must be numbered consecutively from 1")
    stations[-1]["next"] = 1
    result["loop"]["stations"] = stations
    result["loop"]["source_urls"] = [s["url"] for s in sources(loop)]

    levels = list(re.finditer(r"^## Level (\d+)\. ([^\n]+)\n(.*?)(?=^## |\Z)", curriculum, re.M | re.S))
    if [int(m[1]) for m in levels] != [level["level"] for level in result["study_path"]]:
        raise ValueError("curriculum and index levels differ")
    for match, level in zip(levels, result["study_path"]):
        level["name"] = match[2]
        level["sources"] = sources(match[3])
    result["curriculum_source_urls"] = [s["url"] for s in sources(curriculum)]
    return result


def main():
    path = ROOT / "ai-index.json"
    current = json.loads(path.read_text(encoding="utf-8"))
    expected = synchronize(current, *((ROOT / name).read_text(encoding="utf-8")
                                      for name in ("FOUNDATION.md", "LOOP.md", "CURRICULUM.md")))
    if "--check" in sys.argv:
        if current != expected:
            print("ai-index.json differs from its sources; run python3 tools/sync_ai_index.py")
            return 1
        print("four foundations, loop stations and curriculum source links match their documents")
        return 0
    path.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated ai-index.json from FOUNDATION.md, LOOP.md and CURRICULUM.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
