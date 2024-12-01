import unittest
from events.day1.question1 import parse, sort_arrays, get_distance
from events.day1.question2 import calculate_similarity

INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

class TestQuestion1(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(INPUT).shape, (6,2))

    def test_sort(self):
        self.assertEqual(sort_arrays([[2,5],[1,3]]).tolist(),[[1,3],[2,5]])

    def test_distance(self):
        self.assertEqual(get_distance(sort_arrays(parse(INPUT))),11)

class TestQuestion2(unittest.TestCase):
    def test_calculate_similarity(self):
        arr = parse(INPUT)
        self.assertEqual(calculate_similarity(arr),31)