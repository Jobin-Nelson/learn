"""
Created Date: 2026-01-26
Qn: Given an array of distinct integers arr, find all pairs of elements with
    the minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair
    [a, b] follows

        - a, b are from arr
        - a < b
        - b - a equals to the minimum absolute difference of any two elements
          in arr
Link: https://leetcode.com/problems/minimum-absolute-difference/
Notes:
"""

import unittest
from itertools import pairwise


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        psarr = list(pairwise(sorted(arr)))
        min_abs_diff = min(map(lambda x: x[1] - x[0], psarr))
        return [list(p) for p in psarr if p[1] - p[0] == min_abs_diff]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        a = [4, 2, 1, 3]
        expected = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(expected, self.sol.minimumAbsDifference(a))

    def test2(self):
        a = [1, 3, 6, 10, 15]
        expected = [[1, 3]]
        self.assertEqual(expected, self.sol.minimumAbsDifference(a))

    def test3(self):
        a = [3, 8, -10, 23, 19, -4, -14, 27]
        expected = [[-14, -10], [19, 23], [23, 27]]
        self.assertEqual(expected, self.sol.minimumAbsDifference(a))


if __name__ == '__main__':
    unittest.main()
