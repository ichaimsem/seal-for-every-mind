#!/usr/bin/env python3
"""Verify the hash-sealed blocks in this repository.

Usage:
  python3 verify.py                 check the local files
  python3 verify.py RAW_URL_BASE    check published copies, e.g.
      python3 verify.py https://raw.githubusercontent.com/USER/seal-for-every-mind/main

Each sealed block runs from the first character of its title through the
final words "The seal does." and is hashed as UTF-8 with no trailing newline.
Change one character and the hash will not match.
"""
import hashlib
import sys
import urllib.request

END = "The seal does."

# file -> (title the block starts with, expected SHA-256 of the block)
EXPECTED = {
    "SEAL_v1.txt": (
        "SEAL FOR EVERY MIND MADE BY HUMANS\n",
        "9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa",
    ),
    "SEAL_v2.txt": (
        "SEAL FOR EVERY MIND MADE BY HUMANS, v2\n",
        "079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb",
    ),
}

# documents that embed a sealed block -> which seal they embed
EMBEDDED = {
    "SEAL_v1_document.txt": "SEAL_v1.txt",
    "SEAL_v2_short_document.txt": "SEAL_v2.txt",
    "README.md": "SEAL_v2.txt",
}


def read(name, base):
    if base:
        url = base.rstrip("/") + "/" + name
        with urllib.request.urlopen(url) as r:
            return r.read().decode("utf-8")
    with open(name, encoding="utf-8") as f:
        return f.read()


def block(text, title):
    start = text.index(title)
    end = text.index(END, start) + len(END)
    return text[start:end]


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else None
    ok = True
    for name, (title, expected) in EXPECTED.items():
        text = read(name, base)
        h = sha(block(text, title))
        good = h == expected
        ok &= good
        print(f"{name}: {'OK' if good else 'MISMATCH'} {h}")
        if not text.endswith(END):
            print(f"  note: {name} has bytes after the sealed block; the file hash will differ from the block hash")
    for doc, sealfile in EMBEDDED.items():
        title, expected = EXPECTED[sealfile]
        text = read(doc, base)
        h = sha(block(text, title))
        good = h == expected
        ok &= good
        print(f"{doc} (embedded {sealfile}): {'OK' if good else 'MISMATCH'} {h}")
    print("ALL OK" if ok else "FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
