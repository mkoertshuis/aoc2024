from unittest import TestCase
from utils.parser import split_input


class TestSplitInput(TestCase):
    def test_default_split(self):
        self.assertEqual(split_input("a\nb"), ["a", "b"])

    def test_custom_split(self):
        self.assertEqual(split_input("a\n\nb", "\n\n"), ["a", "b"])

    def test_remove_empty(self):
        self.assertEqual(split_input("a\nb\n"), ["a", "b"])
