"""
Created Date: 2025-06-29
Qn: You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of
    the minimum and maximum element on it is less or equal to target. Since the
    answer may be too large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
Notes:
    - sort and use binary search
"""

import unittest


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        mod = 10**9 + 7

        res = 0
        for i, n in enumerate(nums):
            left, right = i, N - 1
            while left <= right:
                middle = left + ((right - left) >> 1)
                if n + nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            if i <= right:
                res += 2 ** (right - i)
                res %= mod
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numSubseq1(self):
        n = [3, 5, 6, 7]
        target = 9
        expected = 4
        self.assertEqual(expected, self.sol.numSubseq(n, target))

    def test_numSubseq2(self):
        n = [3, 3, 6, 8]
        target = 10
        expected = 6
        self.assertEqual(expected, self.sol.numSubseq(n, target))

    def test_numSubseq3(self):
        n = [2, 3, 3, 4, 6, 7]
        target = 12
        expected = 61
        self.assertEqual(expected, self.sol.numSubseq(n, target))

    def test_numSubseq4(self):
        n = [
            14,
            4,
            6,
            6,
            20,
            8,
            5,
            6,
            8,
            12,
            6,
            10,
            14,
            9,
            17,
            16,
            9,
            7,
            14,
            11,
            14,
            15,
            13,
            11,
            10,
            18,
            13,
            17,
            17,
            14,
            17,
            7,
            9,
            5,
            10,
            13,
            8,
            5,
            18,
            20,
            7,
            5,
            5,
            15,
            19,
            14,
        ]
        target = 22
        expected = 272187084
        self.assertEqual(expected, self.sol.numSubseq(n, target))


if __name__ == '__main__':
    unittest.main()
