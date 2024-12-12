import unittest
from events.day9.question1 import main as main1
from events.day9.question2 import main as main2

raw_input = "2333133121414131402"


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 1928)


# class TestQuestion2(unittest.TestCase):
#     def test_answer(self):
#         self.assertEqual(main2(raw_input), 34)
