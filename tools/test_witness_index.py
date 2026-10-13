"""Regression tests for the witness ledger check added on 12 October 2026.

A witness record is evidence and the index is the ledger that points at it. These
tests fix the behaviour in place: a disagreement fails the build, a missing field
only warns, and no test ever rewrites a record to make a check pass.
"""
import hashlib
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("qa", Path(__file__).with_name("qa.py"))
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)

SEAL = hashlib.sha256(b"a seal").hexdigest()
COLUMNS = "| date | provider | model | version | status | file |"


def record(provider="nvidia-nim", model="meta/llama-3.2-11b-vision-instruct", date="2026-09-11",
           version="2", status="ok", seal=None, finish_reason='"stop"'):
    lines = ["# Witness reply via API", "", f"provider: {provider}", f"model: {model}",
             f"date: {date}", f"seal_version: {version}",
             f"seal_sha256_shown: {seal or SEAL}", f"status: {status}", ""]
    if finish_reason is not None:
        lines.insert(-1, f"finish_reason: {finish_reason}")
    return "\n".join(lines + ["---", "", "A reply.", ""])


def row(name, provider="nvidia-nim", model="meta/llama-3.2-11b-vision-instruct",
        date="2026-09-11", version="2", status="ok"):
    return f"| {date} | {provider} | {model} | {version} | {status} | witnesses/api/{name} |"


class WitnessIndexTests(unittest.TestCase):
    def setUp(self):
        qa.results.clear()
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self._cwd = os.getcwd()
        os.chdir(self._tmp.name)
        self.addCleanup(os.chdir, self._cwd)
        Path("witnesses/api").mkdir(parents=True)

    def _run(self, index_body, records):
        for name, text in records.items():
            Path("witnesses/api", name).write_text(text, encoding="utf-8")
        Path("witnesses/INDEX.md").write_text("# Witness replies collected via API\n\n"
                                              + COLUMNS + "\n|---|---|---|---|---|---|\n"
                                              + index_body, encoding="utf-8")
        Path("SEAL_v2.txt").write_text("a seal", encoding="utf-8")
        files = ["witnesses/INDEX.md", "SEAL_v2.txt"] + [f"witnesses/api/{n}" for n in records]
        qa.check_witnesses(sorted(files))
        return qa.results[-1]

    def test_index_matching_its_records_passes(self):
        status, _, detail = self._run(row("a.md") + "\n", {"a.md": record()})
        self.assertEqual(status, "OK", detail)
        self.assertIn("1 records", detail)

    def test_failed_request_is_counted_as_failed_not_as_agreement(self):
        status, _, detail = self._run(row("a.md") + "\n" + row("b.md", status="error") + "\n",
                                      {"a.md": record(), "b.md": record(status="error")})
        self.assertEqual(status, "OK", detail)
        self.assertIn("1 with a usable reply", detail)
        self.assertIn("1 failed at the provider", detail)

    def test_status_disagreement_fails_the_build(self):
        status, _, detail = self._run(row("a.md", status="ok") + "\n", {"a.md": record(status="error")})
        self.assertEqual(status, "FAIL")
        self.assertIn("index status='ok' but record status='error'", detail)

    def test_date_disagreement_is_caught_by_column_not_by_position(self):
        status, _, detail = self._run(row("a.md", date="2026-09-12") + "\n", {"a.md": record()})
        self.assertEqual(status, "FAIL")
        self.assertIn("index date='2026-09-12' but record date='2026-09-11'", detail)

    def test_record_missing_from_the_index_fails(self):
        status, _, detail = self._run(row("a.md") + "\n", {"a.md": record(), "b.md": record()})
        self.assertEqual(status, "FAIL")
        self.assertIn("b.md is not listed", detail)

    def test_index_row_pointing_at_a_missing_file_fails(self):
        status, _, detail = self._run(row("gone.md") + "\n", {})
        self.assertEqual(status, "FAIL")
        self.assertIn("gone.md is listed but does not exist", detail)

    def test_repeated_row_fails(self):
        status, _, detail = self._run(row("a.md") + "\n" + row("a.md") + "\n", {"a.md": record()})
        self.assertEqual(status, "FAIL")
        self.assertIn("listed more than once", detail)

    def test_record_of_another_seal_version_fails(self):
        status, _, detail = self._run(row("a.md") + "\n", {"a.md": record(seal="f" * 64)})
        self.assertEqual(status, "FAIL")
        self.assertIn("shows seal hash", detail)

    def test_finish_reason_is_never_required(self):
        # Historical records predate the field and are never rewritten, so it must
        # not raise a warning that no one is permitted to clear.
        status, _, detail = self._run(row("a.md") + "\n", {"a.md": record(finish_reason=None)})
        self.assertEqual(status, "OK", detail)

    def test_missing_required_field_warns_without_failing(self):
        status, _, detail = self._run(row("a.md") + "\n",
                                      {"a.md": record().replace("provider: nvidia-nim\n", "")})
        self.assertEqual(status, "WARN")
        self.assertIn("no provider: line", detail)

    def test_wrong_column_header_fails(self):
        for name, text in {"a.md": record()}.items():
            Path("witnesses/api", name).write_text(text, encoding="utf-8")
        Path("witnesses/INDEX.md").write_text("| date | provider | model | status | file |\n"
                                              "|---|---|---|---|---|\n" + row("a.md") + "\n", encoding="utf-8")
        Path("SEAL_v2.txt").write_text("a seal", encoding="utf-8")
        qa.check_witnesses(["witnesses/INDEX.md", "SEAL_v2.txt", "witnesses/api/a.md"])
        status, _, detail = qa.results[-1]
        self.assertEqual(status, "FAIL")
        self.assertIn("columns are", detail)

    def test_a_failing_check_never_rewrites_a_record(self):
        before = record(status="ok")
        self._run(row("a.md", status="error") + "\n", {"a.md": before})
        self.assertEqual(Path("witnesses/api/a.md").read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
