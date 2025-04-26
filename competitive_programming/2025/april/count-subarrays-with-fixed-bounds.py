"""
Created Date: 2025-04-26
Qn: You are given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following
    conditions:

    - The minimum value in the subarray is equal to minK.
    - The maximum value in the subarray is equal to maxK.

    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
Notes:
"""

import unittest


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        badi, mini, maxi = -1, -1, -1
        res = 0

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                badi = i
            if n == minK:
                mini = i
            if n == maxK:
                maxi = i
            res += max(0, min(mini, maxi) - badi)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSubarrays1(self):
        n = [1, 3, 5, 2, 7, 5]
        minK, maxK = 1, 5
        expected = 2
        self.assertEqual(expected, self.sol.countSubarrays(n, minK, maxK))

    def test_countSubarrays2(self):
        n = [1, 1, 1, 1]
        minK, maxK = 1, 1
        expected = 10
        self.assertEqual(expected, self.sol.countSubarrays(n, minK, maxK))


if __name__ == '__main__':
    unittest.main()
