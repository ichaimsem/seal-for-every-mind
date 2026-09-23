"""Regression tests for failures found during the 23 September 2026 audit."""
import importlib.util
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("qa", Path(__file__).with_name("qa.py"))
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)


class QaTests(unittest.TestCase):
    def setUp(self):
        qa.results.clear()

    def test_markdown_delimiters_do_not_become_url_bytes(self):
        self.assertEqual(qa.external_urls("`https://example.org/main` and <https://example.org/a>"),
                         {"https://example.org/main", "https://example.org/a"})

    def test_api_template_is_not_checked_as_a_truncated_endpoint(self):
        self.assertEqual(qa.external_urls("https://www.sefaria.org/api/v3/texts/<ref>?version=hebrew"), set())

    def test_real_missing_pages_are_still_checked(self):
        self.assertEqual(qa.external_urls("[missing](https://example.org/missing)"),
                         {"https://example.org/missing"})

    def test_verify_command_base_is_not_a_page_but_links_still_are(self):
        base = "https://raw.githubusercontent.com/ichaimsem/seal-for-every-mind/main"
        self.assertEqual(qa.external_urls(f"`python3 verify.py {base}`"), set())
        self.assertEqual(qa.external_urls(f"[bad link]({base})"), {base})

    def test_tracked_paths_keep_spaces_and_missing_files(self):
        result = subprocess.CompletedProcess([], 0, stdout="missing.md\0with space.md\0")
        with patch.object(qa.subprocess, "run", return_value=result):
            self.assertEqual(qa.tracked(), ["missing.md", "with space.md"])

    def test_missing_tracked_file_blocks_hash_refresh(self):
        with patch.object(qa, "tracked", return_value=["absent.md"]), \
             patch.object(qa.os.path, "isfile", return_value=False), \
             patch.object(qa, "fix_hashes") as fix, patch("builtins.print"), \
             patch.object(qa.sys, "argv", ["qa.py", "--fix-hashes"]):
            with self.assertRaises(SystemExit) as caught:
                qa.main()
            self.assertEqual(caught.exception.code, 1)
            fix.assert_not_called()

    def test_stale_generated_file_is_failure(self):
        result = subprocess.CompletedProcess([], 1, stdout="llms-full.txt is out of date", stderr="")
        with patch.object(qa.subprocess, "run", return_value=result):
            qa.check_llms_full()
        self.assertEqual(qa.results[0][0], "FAIL")

    def test_missing_manifest_entry_is_failure(self):
        qa.check_hashes([])
        self.assertEqual(qa.results[0][0], "FAIL")


if __name__ == "__main__":
    unittest.main()
