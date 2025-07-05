"""
Created Date: 2025-06-30
Qn: We define a harmonious array as an array where the difference between its
    maximum value and its minimum value is exactly 1.

    Given an integer array nums, return the length of its longest harmonious
    subsequence among all its possible subsequences.
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        res = 0
        for i, n in freq.items():
            if freq[i+1] > 0:
                res = max(res, n + freq[i+1])
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findLHS1(self):
        n = [1, 3, 2, 2, 5, 2, 3, 7]
        expected = 5
        self.assertEqual(expected, self.sol.findLHS(n))

    def test_findLHS2(self):
        n = [1, 2, 3, 4]
        expected = 2
        self.assertEqual(expected, self.sol.findLHS(n))

    def test_findLHS3(self):
        n = [1] * 4
        expected = 0
        self.assertEqual(expected, self.sol.findLHS(n))


if __name__ == '__main__':
    unittest.main()
