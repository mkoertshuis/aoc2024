import unittest
from events.day12.question1 import main as main1
from events.day12.question2 import main as main2

raw_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 1930)


# class TestQuestion2(unittest.TestCase):
#     def test_answer(self):
#         self.assertEqual(main2(raw_input), 81)
