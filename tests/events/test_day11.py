import unittest
from events.day11.question1 import main as main1
from events.day11.question2 import main as main2

raw_input = "125 17"


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 55312)


# class TestQuestion2(unittest.TestCase):
#     def test_answer(self):
#         self.assertEqual(main2(raw_input), 81)
