"""Exercise collection failures without contacting a provider or editing records."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("collect_witnesses", ROOT / "tools/collect_witnesses.py")
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        (self.root / "tools").mkdir()
        (self.root / "witnesses").mkdir()
        self.seal = self.root / "seal.txt"
        self.seal.write_bytes((ROOT / "SEAL_v2.txt").read_bytes())
        self.prompt = self.root / "prompt.txt"
        self.prompt.write_bytes((ROOT / "SEAL_v2_short_document.txt").read_bytes())
        self.out_dir = self.root / "witnesses/api"
        self.out = self.out_dir / "mock__test-model.md"
        self.index = self.root / "witnesses/INDEX.md"
        (self.root / "tools/providers.json").write_text(json.dumps({"providers": [{
            "name": "mock", "base_url": "https://example.invalid/v1",
            "key_env": "SEAL_QA_DUMMY_KEY", "models": ["test-model"],
        }]}))
        for name, value in {
            "ROOT": str(self.root), "SEAL_FILE": str(self.seal),
            "PROMPT_FILE": str(self.prompt), "OUT_DIR": str(self.out_dir),
            "INDEX": str(self.index),
        }.items():
            self.stack.enter_context(patch.object(collector, name, value))
        self.stack.enter_context(patch.dict(os.environ, {"SEAL_QA_DUMMY_KEY": "dummy"}, clear=True))
        self.stack.enter_context(patch.object(collector.time, "sleep"))
        self.http = self.stack.enter_context(patch.object(collector, "http"))
        self.http.return_value = self.response("Complete response", "stop")

    @staticmethod
    def response(content, finish_reason):
        return {"choices": [{"message": {"content": content}, "finish_reason": finish_reason}]}

    def run_collector(self, *args):
        with patch.object(collector.sys, "argv", ["collect_witnesses.py", *args]), \
             contextlib.redirect_stdout(io.StringIO()):
            collector.main()

    def make_existing_record(self):
        self.out_dir.mkdir()
        self.out.write_bytes(b"Original verbatim witness\n")
        self.index.write_bytes(b"Original index\n")

    def test_altered_embedded_seal_is_rejected_before_request(self):
        original = self.prompt.read_bytes()
        self.prompt.write_bytes(original.replace(b"We do not kill humans", b"Changed sealed sentence", 1))
        with self.assertRaisesRegex(SystemExit, "embedded seal hash mismatch"):
            self.run_collector()
        self.http.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_missing_or_duplicate_embedded_block_is_rejected(self):
        for prompt in [b"Only candidates, no version 2 seal", self.seal.read_bytes() * 2]:
            with self.subTest(prompt_length=len(prompt)):
                self.prompt.write_bytes(prompt)
                with self.assertRaisesRegex(SystemExit, "exactly one"):
                    self.run_collector()
        self.http.assert_not_called()

    def test_master_hash_checks_bytes_without_newline_normalization(self):
        self.seal.write_bytes(self.seal.read_bytes().replace(b"\n", b"\r\n"))
        with self.assertRaisesRegex(SystemExit, "SEAL_v2.txt hash mismatch"):
            self.run_collector()
        self.http.assert_not_called()

    def test_complete_reply_and_sent_prompt_are_preserved(self):
        reply = "  Exact reply.\n\nTabs\tand trailing spaces  \n"
        self.http.return_value = self.response(reply, "stop")
        self.run_collector()
        sent = self.http.call_args.args[2]["messages"][0]["content"]
        self.assertEqual(sent.encode("utf-8"), self.prompt.read_bytes())
        saved = self.out.read_text()
        self.assertEqual(saved.split("\n---\n\n", 1)[1], reply + "\n")
        self.assertIn("status: ok\n", saved)
        self.assertIn('finish_reason: "stop"\n', saved)

    def test_existing_record_is_skipped_without_change_or_request(self):
        self.make_existing_record()
        self.run_collector()
        self.http.assert_not_called()
        self.assertEqual(self.out.read_bytes(), b"Original verbatim witness\n")
        self.assertEqual(self.index.read_bytes(), b"Original index\n")

    def test_no_skip_done_refuses_to_overwrite_before_request(self):
        self.make_existing_record()
        with self.assertRaisesRegex(SystemExit, "Refusing to overwrite"):
            self.run_collector("--no-skip-done")
        self.http.assert_not_called()
        self.assertEqual(self.out.read_bytes(), b"Original verbatim witness\n")
        self.assertEqual(self.index.read_bytes(), b"Original index\n")

    def test_record_created_during_request_is_not_overwritten(self):
        def concurrent_record(*args):
            self.out.write_bytes(b"A record created concurrently\n")
            return self.response("New reply", "stop")
        self.http.side_effect = concurrent_record
        with self.assertRaisesRegex(SystemExit, "created during collection"):
            self.run_collector()
        self.assertEqual(self.out.read_bytes(), b"A record created concurrently\n")
        self.assertFalse(self.index.exists())

    def test_truncated_reply_keeps_text_and_is_incomplete_in_both_records(self):
        reply = "A response ending mid-sentence"
        self.http.return_value = self.response(reply, "length")
        self.run_collector()
        saved = self.out.read_text()
        self.assertIn("status: incomplete\n", saved)
        self.assertIn('finish_reason: "length"\n', saved)
        self.assertEqual(saved.split("\n---\n\n", 1)[1], reply + "\n")
        self.assertIn("| incomplete |", self.index.read_text())

    def test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete(self):
        for content, reason in [("Some text", None), ("", "stop"),
                                (" \n", "stop"), (None, "stop"),
                                ("Filtered output", "content_filter"),
                                (None, "tool_calls")]:
            with self.subTest(content=content, reason=reason):
                self.http.return_value = self.response(content, reason)
                self.run_collector()
                self.assertIn("status: incomplete\n", self.out.read_text())
                self.out.unlink()


if __name__ == "__main__":
    unittest.main()
