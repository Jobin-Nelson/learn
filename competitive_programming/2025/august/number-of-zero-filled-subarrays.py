"""
Created Date: 2025-08-19
Qn: Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
Notes:
    - use sum of first natural numbers
"""

import unittest
from itertools import groupby


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        # Functional approach
        range_sum = lambda x: x * (x + 1) >> 1
        return sum(range_sum(len(list(g))) for v, g in groupby(nums) if v == 0)

        # Imperative approach
        # res = 0
        # streak = 0
        # for n in nums:
        #     if n != 0:
        #         if streak != 0:
        #             res += (streak * (streak + 1) >> 1)
        #         streak = 0
        #     elif n == 0:
        #         streak += 1
        # if streak != 0:
        #     res += (streak * (streak + 1) >> 1)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zeroFilledSubarray1(self):
        n = [1, 3, 0, 0, 2, 0, 0, 4]
        expected = 6
        self.assertEqual(expected, self.sol.zeroFilledSubarray(n))

    def test_zeroFilledSubarray2(self):
        n = [0, 0, 0, 2, 0, 0]
        expected = 9
        self.assertEqual(expected, self.sol.zeroFilledSubarray(n))

    def test_zeroFilledSubarray3(self):
        n = [2, 10, 2019]
        expected = 0
        self.assertEqual(expected, self.sol.zeroFilledSubarray(n))


if __name__ == '__main__':
    unittest.main()
