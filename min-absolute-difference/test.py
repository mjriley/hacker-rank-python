import unittest

from .solution import minimumAbsoluteDifference


class TestSolution(unittest.TestCase):

    def test_computes_diff_between_two_numbers(self):
        self.assertEqual(minimumAbsoluteDifference([2, 3]), 1)

    def test_computes_absolute_diff(self):
        self.assertEqual(minimumAbsoluteDifference([2, 3]), 1)
        self.assertEqual(minimumAbsoluteDifference([3, 2]), 1)

    def test_finds_min_diff_from_unsorted_array(self):
        self.assertEqual(minimumAbsoluteDifference([10, 2, 6, 0]), 2)

    def test_supports_negative_numbers(self):
        self.assertEqual(minimumAbsoluteDifference([10, -2, -5]), 3)

    def test_example_1(self):
        self.assertEqual(minimumAbsoluteDifference([3, -7, 0]), 3)

    def test_example_2(self):
        self.assertEqual(minimumAbsoluteDifference(
            [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)

    def test_example_3(self):
        self.assertEqual(minimumAbsoluteDifference([1, -3, 71, 68, 17]), 3)
