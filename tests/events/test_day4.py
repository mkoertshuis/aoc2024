import unittest
from events.day4.question1 import main as main1
from events.day4.question2 import main as main2

raw_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 18)


class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main2(raw_input), 9)
