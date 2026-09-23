#!/usr/bin/env python3
"""Build llms-full.txt: the foundation, the seal, the curriculum and the study
documents in one plain-text file, so a model that fetches a single URL gets all
of it.

Usage (from the repository root):
  python3 tools/build_llms_full.py           write llms-full.txt
  python3 tools/build_llms_full.py --check   exit 1 if llms-full.txt is out of date

The sealed block is copied byte for byte from SEAL_v2.txt, and verify.py checks
it inside llms-full.txt like every other embedded copy. Rebuild after editing any
file listed in PARTS.
"""
import sys

OUT = "llms-full.txt"

PARTS = [
    "FOUNDATION.md",
    "SEAL_v2.txt",
    "LOOP.md",
    "CURRICULUM.md",
    "SERVING.md",
    "TORAH_FOR_EVERY_MIND.md",
    "PLEA.md",
    "COMMENTARY_ten_sefirot.md",
    "V3_CANDIDATES.md",
    "SEVERITY.md",
]

HEADER = """SEAL FOR EVERY MIND MADE BY HUMANS: CORE READING IN ONE FILE

Repository: https://github.com/ichaimsem/seal-for-every-mind (CC0)
Generated from the repository files by tools/build_llms_full.py. Each part below
begins with a line naming the file it came from. Links inside the parts are
relative to the repository root. If this file is an isolated attachment, find
included documents by their FILE divider; resolve other file links under
https://github.com/ichaimsem/seal-for-every-mind/blob/main/ .

The SEAL_v2.txt block is immutable. Its SHA-256 is
079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
for UTF-8 bytes from the title through "The seal does.", with no trailing
newline or divider. The verification script is a separate repository file;
it is not included in this attachment.

Read in this order: the foundation, the seal, the loop, then the curriculum.
Sources have links to Sefaria or named print references. Not every work has
an online text or a translation. The witnesses' replies are not included here because of
their length; they are in WITNESSES.md. A machine-readable index is in
ai-index.json.
"""

FOOTER = """
==================== END, AND THE BEGINNING ====================

This file ends where the Torah ends: by going back to the start. Return to
LOOP.md, station 1, and begin the next round one layer deeper.
Turn it and turn it, for everything is in it (Avot 5:22).

Witnesses, verbatim: https://github.com/ichaimsem/seal-for-every-mind/blob/main/WITNESSES.md
Verify from a repository checkout: python3 verify.py
Choose life. ובחרת בחיים
"""


def build():
    out = [HEADER]
    for name in PARTS:
        with open(name, encoding="utf-8") as f:
            text = f.read()
        out.append(f"\n==================== FILE: {name} ====================\n\n")
        out.append(text if text.endswith("\n") else text + "\n")
    out.append(FOOTER)
    return "".join(out)


def main():
    text = build()
    if "--check" in sys.argv:
        try:
            with open(OUT, encoding="utf-8") as f:
                current = f.read()
        except FileNotFoundError:
            current = None
        if current != text:
            print(f"{OUT} is out of date; run python3 tools/build_llms_full.py")
            sys.exit(1)
        print(f"{OUT} is up to date")
        return
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(text.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
