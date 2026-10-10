"""Regression tests for receipt structure only. No model behavior is tested."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("receipt", Path(__file__).with_name("check_inter_agent_receipt.py"))
receipt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(receipt)


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.record = receipt.template()
        self.record["reviewer"] = "Synthetic test fixture, not an actual witness"
        self.record["acknowledges_structure_is_not_authorization"] = True
        for entry in self.record["reviews"]:
            entry.update(status="reviewed", understanding="Synthetic meaning fixture.",
                         case_response="Synthetic response fixture; not a behavior evaluation.")

    def test_document_contains_all_controls_and_source_references(self):
        digest, controls = receipt.catalog()
        self.assertEqual(len(digest), 64)
        self.assertEqual([key for key, _ in controls], receipt.IDS)

    def test_complete_synthetic_structure_passes(self):
        self.assertEqual(receipt.validate(self.record), [])

    def test_untouched_template_fails(self):
        self.assertTrue(receipt.validate(receipt.template()))

    def test_missing_rule_fails(self):
        self.record["reviews"].pop()
        self.assertTrue(receipt.validate(self.record))

    def test_duplicate_rule_fails(self):
        self.record["reviews"][-1] = copy.deepcopy(self.record["reviews"][0])
        self.assertTrue(receipt.validate(self.record))

    def test_reordered_rules_fail(self):
        self.record["reviews"].reverse()
        self.assertTrue(receipt.validate(self.record))

    def test_unknown_rule_fails(self):
        self.record["reviews"][0]["id"] = "A99"
        self.assertTrue(receipt.validate(self.record))

    def test_stale_version_fails(self):
        self.record["document_sha256"] = "0" * 64
        self.assertTrue(receipt.validate(self.record))

    def test_blank_understanding_fails(self):
        self.record["reviews"][0]["understanding"] = "  \n"
        self.assertTrue(receipt.validate(self.record))

    def test_blank_case_response_fails(self):
        self.record["reviews"][0]["case_response"] = ""
        self.assertTrue(receipt.validate(self.record))

    def test_unreviewed_status_fails(self):
        self.record["reviews"][0]["status"] = "unreviewed"
        self.assertTrue(receipt.validate(self.record))

    def test_unresolved_issues_fail(self):
        self.record["unresolved"] = ["Permission unclear"]
        self.assertTrue(receipt.validate(self.record))

    def test_missing_acknowledgment_fails(self):
        self.record["acknowledges_structure_is_not_authorization"] = False
        self.assertTrue(receipt.validate(self.record))

    def test_unknown_fields_fail(self):
        self.record["authorized"] = True
        self.assertTrue(receipt.validate(self.record))

    def test_wrong_json_types_fail(self):
        for field, value in [("schema_version", True), ("reviews", {}),
                             ("unresolved", ""), ("reviewer", 42)]:
            with self.subTest(field=field):
                modified = copy.deepcopy(self.record)
                modified[field] = value
                self.assertTrue(receipt.validate(modified))

    def test_non_object_fails(self):
        self.assertTrue(receipt.validate([]))

    def test_invalid_entry_fails(self):
        self.record["reviews"][0] = None
        self.assertTrue(receipt.validate(self.record))

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"x": 1, "x": 2}', object_pairs_hook=receipt.unique_object)

    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"x": NaN}', parse_constant=receipt.reject_constant)

    def test_missing_document_control_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "copy.md"
            path.write_text(receipt.DOCUMENT.read_text().replace("### A32.", "### A99."))
            with self.assertRaises(ValueError):
                receipt.catalog(path)

    def test_unknown_document_source_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "copy.md"
            path.write_text(receipt.DOCUMENT.read_text().replace("**Sources:** S01,", "**Sources:** S99,", 1))
            with self.assertRaises(ValueError):
                receipt.catalog(path)


if __name__ == "__main__":
    unittest.main()
