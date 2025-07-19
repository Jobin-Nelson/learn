"""
Created Date: 2025-07-17
Qn: You are given an integer array nums and a positive integer k.
    A subsequence sub of nums with length x is called valid if it satisfies:

    - (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] +
      sub[x - 1]) % k.

    Return the length of the longest valid subsequence of nums.
Link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/
Notes:
"""

import unittest


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for n in nums:
            n %= k
            for prev in range(k):
                dp[prev][n] = dp[n][prev] + 1
                res = max(res, dp[prev][n])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumLength1(self):
        n = list(range(1, 6))
        k = 2
        expected = 5
        self.assertEqual(expected, self.sol.maximumLength(n, k))

    def test_maximumLength2(self):
        n = [1, 4, 2, 3, 1, 4]
        k = 3
        expected = 4
        self.assertEqual(expected, self.sol.maximumLength(n, k))


if __name__ == '__main__':
    unittest.main()
