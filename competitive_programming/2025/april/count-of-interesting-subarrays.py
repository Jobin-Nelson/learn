"""
Created Date: 2025-04-25
Qn: You are given a 0-indexed integer array nums, an integer modulo, and an
    integer k.

    Your task is to find the count of subarrays that are interesting.

    A subarray nums[l..r] is interesting if the following condition holds:

    - Let cnt be the number of indices i in the range [l, r] such that nums[i]
      % modulo == k. Then, cnt % modulo == k. Return an integer denoting the
      count of interesting subarrays.

    Note: A subarray is a contiguous non-empty sequence of elements within an
    array.
Link: https://leetcode.com/problems/count-of-interesting-subarrays/
Notes:
    - use prefix counts
"""

import unittest
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        prefix = 0
        res = 0
        n = len(nums)
        count = Counter([0])

        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += count[(prefix - k + modulo) % modulo]
            count[prefix % modulo] += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countInterestingSubarrays1(self):
        n, m, k = [3, 2, 4], 2, 1
        expected = 3
        self.assertEqual(expected, self.sol.countInterestingSubarrays(n, m, k))

    def test_countInterestingSubarrays2(self):
        n, m, k = [3, 1, 9, 6], 3, 0
        expected = 2
        self.assertEqual(expected, self.sol.countInterestingSubarrays(n, m, k))


if __name__ == '__main__':
    unittest.main()
