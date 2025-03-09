"""
Created Date: 2025-03-06
Qn: You are given a 0-indexed 2D integer matrix grid of size n * n with values
    in the range [1, n2]. Each integer appears exactly once except a which appears
    twice and b which is missing. The task is to find the repeating and missing
    numbers a and b.

    Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and
    ans[1] equals to b.
Link: https://leetcode.com/problems/find-missing-and-repeated-values/
Notes:
    - use hashmap or hashset
"""

import unittest
from itertools import chain


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        N = len(grid)
        num_set = set(chain.from_iterable(grid))
        og = set(range(1, (N * N) + 1))
        missing = og - num_set
        common = 0
        for n in chain.from_iterable(grid):
            if n not in og:
                common = n
                break
            og.remove(n)
        return [common] + list(missing)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findMissingAndRepeatedValues1(self):
        g = [[1, 3], [2, 2]]
        expected = [2, 4]
        self.assertEqual(expected, self.sol.findMissingAndRepeatedValues(g))

    def test_findMissingAndRepeatedValues2(self):
        g = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
        expected = [9, 5]
        self.assertEqual(expected, self.sol.findMissingAndRepeatedValues(g))


if __name__ == '__main__':
    unittest.main()
