"""
Created Date: 2025-10-16
Qn: You are given a 0-indexed integer array nums and an integer value.

    In one operation, you can add or subtract value from any element of nums.

    For example, if nums = [1,2,3] and value = 2, you can choose to subtract
    value from nums[0] to make nums = [-1,2,3].

    The MEX (minimum excluded) of an array is the smallest missing non-negative
    integer in it.

    For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.

    Return the maximum MEX of nums after applying the mentioned operation any
    number of times.
Link: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        rem_freq = Counter(n % value for n in nums)
        mex = 0

        while rem_freq[mex % value] > 0:
            rem_freq[mex % value] -= 1
            mex += 1
        return mex


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n, v = [1, -10, 7, 13, 6, 8], 5
        expected = 4
        self.assertEqual(expected, self.sol.findSmallestInteger(n, v))

    def test2(self):
        n, v = [1, -10, 7, 13, 6, 8], 7
        expected = 2
        self.assertEqual(expected, self.sol.findSmallestInteger(n, v))


if __name__ == '__main__':
    unittest.main()
