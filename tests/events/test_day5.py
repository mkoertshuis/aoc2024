import unittest
from events.day5.question1 import main as main1
from events.day5.question2 import main as main2

raw_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


class TestQuestion1(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main1(raw_input), 143)


# class TestQuestion2(unittest.TestCase):
#     def test_answer(self):
#         self.assertEqual(main2(raw_input), 123)