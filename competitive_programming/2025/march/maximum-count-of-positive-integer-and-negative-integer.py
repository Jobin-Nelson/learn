"""
Created Date: 2025-03-12
Qn: Given an array nums sorted in non-decreasing order, return the maximum
    between the number of positive integers and the number of negative
    integers.

    In other words, if the number of positive integers in nums is pos and the
    number of negative integers is neg, then return the maximum of pos and neg.
    Note that 0 is neither positive nor negative.
Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
Notes:
"""

import unittest


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        return max(
            sum(1 for n in nums if n < 0),
            sum(1 for n in nums if n > 0)
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumCount1(self):
        n = [-2, -1, -1, 1, 2, 3]
        expected = 3
        self.assertEqual(expected, self.sol.maximumCount(n))

    def test_maximumCount2(self):
        n = [-3, -2, -1, 0, 0, 1, 2]
        expected = 3
        self.assertEqual(expected, self.sol.maximumCount(n))

    def test_maximumCount3(self):
        n = [5, 20, 66, 1314]
        expected = 4
        self.assertEqual(expected, self.sol.maximumCount(n))


if __name__ == '__main__':
    unittest.main()
