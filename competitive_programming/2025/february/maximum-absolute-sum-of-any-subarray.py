"""
Created Date: 2025-02-26
Qn: You are given an integer array nums. The absolute sum of a subarray [numsl,
    numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 +
    numsr).

    Return the maximum absolute sum of any (possibly empty) subarray of nums.

    Note that abs(x) is defined as follows:

    - If x is a negative integer, then abs(x) = -x.
    - If x is a non-negative integer, then abs(x) = x.
Link: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
Notes:
"""

import unittest
from itertools import accumulate
from functools import reduce


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        # Imperative approach
        max_pre, min_pre = 0, 0
        res = 0
        cur = 0
        for n in nums:
            cur += n
            res = max(res, abs(cur - max_pre), abs(cur - min_pre))
            max_pre = max(max_pre, cur)
            min_pre = min(min_pre, cur)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxAbsoluteSum1(self):
        n = [1, -3, 2, 3, -4]
        expected = 5
        self.assertEqual(expected, self.sol.maxAbsoluteSum(n))

    def test_maxAbsoluteSum2(self):
        n = [2, -5, 1, -4, 3, -2]
        expected = 8
        self.assertEqual(expected, self.sol.maxAbsoluteSum(n))


if __name__ == '__main__':
    unittest.main()
