import unittest
from events.day7.question1 import main as main1
from events.day7.question2 import main as main2

raw_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 3749)

class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main2(raw_input), 11387)
