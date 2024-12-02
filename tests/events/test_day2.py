import unittest
from events.day2.question1 import sum_safe
from events.day2.question2 import sum_safe_dampener
from utils.parser import split_input

raw_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        arr = split_input(raw_input)
        self.assertEqual(sum_safe(arr), 2)

class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        arr = split_input(raw_input)
        self.assertEqual(sum_safe_dampener(arr), 4)

