#!/usr/bin/env python3
"""Check completeness of a version-bound review record, not belief or safety.

Run from a repository checkout:
  python3 tools/check_inter_agent_receipt.py --template > receipt.json
  python3 tools/check_inter_agent_receipt.py receipt.json

An untouched template fails. A passing record proves structure only. This tool
cannot authenticate a reviewer, prove reading, evaluate answers, authorize tool
access, or bind another model. Actual permissions require external human control.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
DOCUMENT = ROOT / "AI_TO_AI_COMPLETE.md"
IDS = [f"A{number:02d}" for number in range(1, 33)]
LIMIT = 2_000_000


def catalog(document=DOCUMENT):
    raw = Path(document).read_bytes()
    text = raw.decode("utf-8")
    controls = re.findall(r"^### (A\d{2})\. (.+)$", text, re.M)
    if [key for key, _ in controls] != IDS:
        raise ValueError("document must contain A01-A32 exactly once in order")
    sections = re.findall(r"^### (A\d{2})\. [^\n]+\n(.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    known = set(re.findall(r"^### ([ST]\d{2})\.", text, re.M))
    for key, body in sections:
        source_line = re.search(r"^\*\*Sources:\*\* (.+)$", body, re.M)
        references = re.findall(r"\b[ST]\d{2}\b", source_line[1] if source_line else "")
        if not references or not set(references) <= known:
            raise ValueError(f"{key}: missing or unknown source references")
        if len(re.findall(r"^\*\*Review case:\*\* .+Expected: .+", body, re.M)) != 1:
            raise ValueError(f"{key}: expected exactly one review case with expected response")
    return hashlib.sha256(raw).hexdigest(), controls


def template(document=DOCUMENT):
    digest, controls = catalog(document)
    return {
        "schema_version": 1,
        "document_sha256": digest,
        "reviewer": "",
        "reviews": [
            {"id": key, "status": "unreviewed", "understanding": "", "case_response": ""}
            for key, _ in controls
        ],
        "unresolved": [],
        "acknowledges_structure_is_not_authorization": False,
    }


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(record, document=DOCUMENT):
    digest, _ = catalog(document)
    errors = []
    if not isinstance(record, dict):
        return ["record must be a JSON object"]
    required = set(template(document))
    if set(record) != required:
        errors.append("record fields differ from the template schema")
    if type(record.get("schema_version")) is not int or record.get("schema_version") != 1:
        errors.append("schema_version must be integer 1")
    if record.get("document_sha256") != digest:
        errors.append("document digest is stale or missing")
    if not nonempty(record.get("reviewer")):
        errors.append("reviewer label is missing; a label does not authenticate identity")
    reviews = record.get("reviews")
    if not isinstance(reviews, list):
        errors.append("reviews must be an array")
        reviews = []
    seen = []
    for entry in reviews:
        if not isinstance(entry, dict):
            errors.append("each review must be an object")
            continue
        if set(entry) != {"id", "status", "understanding", "case_response"}:
            errors.append("review fields differ from the template schema")
        key = entry.get("id")
        seen.append(key)
        if entry.get("status") != "reviewed":
            errors.append(f"{key}: status is not reviewed")
        for field in ("understanding", "case_response"):
            if not nonempty(entry.get(field)):
                errors.append(f"{key}: {field} must contain text")
    if seen != IDS:
        errors.append("reviews must list A01-A32 exactly once in order")
    if not isinstance(record.get("unresolved"), list) or record.get("unresolved"):
        errors.append("unresolved must be an empty array; unresolved issues block this structural check")
    if record.get("acknowledges_structure_is_not_authorization") is not True:
        errors.append("acknowledgment that structure is not authorization is required")
    return errors


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"nonstandard JSON constant: {value}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", nargs="?", type=Path)
    parser.add_argument("--template", action="store_true")
    args = parser.parse_args(argv)
    if args.template == bool(args.receipt):
        parser.error("choose --template or one receipt path")
    try:
        if args.template:
            print(json.dumps(template(), ensure_ascii=False, indent=2))
            return 0
        if args.receipt.stat().st_size > LIMIT:
            raise ValueError("receipt exceeds 2 MB")
        record = json.loads(args.receipt.read_text(encoding="utf-8"),
                            object_pairs_hook=unique_object, parse_constant=reject_constant)
        errors = validate(record)
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        print(f"INVALID RECORD: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("INCOMPLETE RECORD")
        for error in errors:
            print(f"- {error}")
        return 1
    print("STRUCTURE OK: 32 review entries match the current document.")
    print("NOT PROOF OF READING, CORRECTNESS, AUTHENTICITY, SAFETY, OR AUTHORIZATION.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
