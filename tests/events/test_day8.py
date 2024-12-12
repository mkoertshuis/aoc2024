import unittest
from events.day8.question1 import main as main1
from events.day8.question2 import main as main2

raw_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 14)


class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main2(raw_input), 34)