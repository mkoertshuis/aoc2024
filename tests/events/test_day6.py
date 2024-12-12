import unittest
from events.day6.question1 import main as main1
from events.day6.question2 import main as main2

raw_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 41)


class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main2(raw_input), 6)
