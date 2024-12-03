import unittest
from events.day3.question1 import main as main1
from events.day3.question2 import main as main2


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        raw_input = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        self.assertEqual(main1(raw_input), 161)


class TestQuestion2(unittest.TestCase):
    def test_answer(self):
        raw_input = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        self.assertEqual(main2(raw_input), 48)
