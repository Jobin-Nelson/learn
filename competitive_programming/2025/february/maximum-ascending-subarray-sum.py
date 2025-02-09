"""
Created Date: 2025-02-04
Qn: Given an array of positive integers nums, return the maximum possible sum
    of an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
    where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
    ascending.
Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/
Notes:
"""

import unittest
from itertools import accumulate, pairwise


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        # Functional approach
        def count(acc: int, val: tuple[int, int]) -> int:
            return acc + val[1] if val[0] < val[1] else val[1]

        return max(accumulate(pairwise(nums), count, initial=nums[0]))

        # Imperative approach
        # cur_count = nums[0]
        # res = nums[0]
        # for i, n in enumerate(nums[:-1]):
        #     if n < nums[i+1]:
        #         cur_count += nums[i+1]
        #     else:
        #         cur_count = nums[i+1]
        #     res = max(res, cur_count)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxAscendingSum1(self):
        n = [10, 20, 30, 5, 10, 50]
        expected = 65
        self.assertEqual(expected, self.sol.maxAscendingSum(n))

    def test_maxAscendingSum2(self):
        n = [10, 20, 30, 40, 50]
        expected = 150
        self.assertEqual(expected, self.sol.maxAscendingSum(n))

    def test_maxAscendingSum3(self):
        n = [12, 17, 15, 13, 10, 11, 12]
        expected = 33
        self.assertEqual(expected, self.sol.maxAscendingSum(n))


if __name__ == '__main__':
    unittest.main()
