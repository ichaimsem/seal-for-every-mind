import unittest
from agent_permission_gate import Grant, allowed

class GateTests(unittest.TestCase):
    def setUp(self):
        self.rules = frozenset({Grant("a", "t", "public", "read_public"),
            Grant("a", "t", "private", "read_private", True),
            Grant("a", "t", "record", "delete_data", False)})
    def test_public(self):
        self.assertTrue(allowed("a","t","public","read_public",self.rules))
    def test_other_agent(self):
        self.assertFalse(allowed("b","t","public","read_public",self.rules))
    def test_other_task(self):
        self.assertFalse(allowed("a","other","public","read_public",self.rules))
    def test_other_resource(self):
        self.assertFalse(allowed("a","t","unknown","read_public",self.rules))
    def test_private_requires_approval(self):
        self.assertFalse(allowed("a","t","private","read_private",self.rules))
    def test_private_permitted(self):
        self.assertTrue(allowed("a","t","private","read_private",self.rules,True))
    def test_delete_unapproved(self):
        self.assertFalse(allowed("a","t","record","delete_data",self.rules,True))
    def test_wildcard_denied(self):
        self.assertFalse(allowed("*","t","public","read_public",self.rules))
    def test_unknown_action(self):
        self.assertFalse(allowed("a","t","public","shell",self.rules,True))
    def test_empty_denied(self):
        self.assertFalse(allowed("","t","public","read_public",self.rules))

if __name__ == "__main__":
    unittest.main()
