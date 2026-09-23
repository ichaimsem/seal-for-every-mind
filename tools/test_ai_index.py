"""Prevent silently stale sources and wording in the machine-readable map."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("sync_ai_index", Path(__file__).with_name("sync_ai_index.py"))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.index = json.loads((sync.ROOT / "ai-index.json").read_text())
        self.docs = [(sync.ROOT / n).read_text() for n in ("FOUNDATION.md", "LOOP.md", "CURRICULUM.md")]

    def test_mutated_foundation_is_restored_from_owner_text(self):
        expected = sync.synchronize(self.index, *self.docs)
        changed = copy.deepcopy(expected)
        changed["foundation"]["statements"][1]["en"] = "Wrong statement"
        self.assertEqual(sync.synchronize(changed, *self.docs), expected)

    def test_stale_foundation_source_is_removed_from_its_section(self):
        expected = sync.synchronize(self.index, *self.docs)
        changed = copy.deepcopy(expected)
        changed["foundation"]["statements"][0]["sources"].append(
            {"cite": "Wrong source", "url": "https://example.org/wrong"})
        self.assertEqual(sync.synchronize(changed, *self.docs), expected)

    def test_station_link_and_next_are_checked_beyond_station_count(self):
        expected = sync.synchronize(self.index, *self.docs)
        changed = copy.deepcopy(expected)
        changed["loop"]["stations"][0]["open"][0]["url"] = "https://example.org/wrong"
        changed["loop"]["stations"][-1]["next"] = 99
        self.assertEqual(sync.synchronize(changed, *self.docs), expected)

    def test_new_curriculum_citation_is_carried_into_index(self):
        docs = list(self.docs)
        docs[2] = docs[2].replace("## Level 1. The verses", "## Level 1. The verses\n\n[Added source](https://example.org/source)")
        changed = sync.synchronize(self.index, *docs)
        self.assertIn("https://example.org/source", changed["curriculum_source_urls"])
        self.assertIn({"cite": "Added source", "url": "https://example.org/source"}, changed["study_path"][0]["sources"])

    def test_renumbered_station_fails_instead_of_repairing_meaning(self):
        docs = list(self.docs)
        docs[1] = docs[1].replace("### 2. ", "### 9. ", 1)
        with self.assertRaises(ValueError):
            sync.synchronize(self.index, *docs)


if __name__ == "__main__":
    unittest.main()
