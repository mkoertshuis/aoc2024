import unittest
from events.day10.question1 import main as main1
from events.day10.question2 import main as main2

raw_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 36)


class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main2(raw_input), 81)
