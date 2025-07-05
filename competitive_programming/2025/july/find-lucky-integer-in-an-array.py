"""
Created Date: 2025-07-05
Qn: Given an array of integers arr, a lucky integer is an integer that has a
    frequency in the array equal to its value.

    Return the largest lucky integer in the array. If there is no lucky integer
    return -1.
Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max(
            (num for num, freq in Counter(arr).items() if num == freq), default=-1
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findLucky1(self):
        a = [2, 2, 3, 4]
        expected = 2
        self.assertEqual(expected, self.sol.findLucky(a))

    def test_findLucky2(self):
        a = [1, 2, 2, 3, 3, 3]
        expected = 3
        self.assertEqual(expected, self.sol.findLucky(a))

    def test_findLucky3(self):
        a = [2, 2, 2, 3, 3]
        expected = -1
        self.assertEqual(expected, self.sol.findLucky(a))


if __name__ == '__main__':
    unittest.main()
