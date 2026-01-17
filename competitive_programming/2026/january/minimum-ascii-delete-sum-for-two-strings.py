"""
Created Date: 2026-01-10
Qn:
Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
Notes:
"""

import unittest


class Solution:
    def MinimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1])
                    )
        return dp[m][n]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s1, s2 = 'sea', 'eat'
        expected = 231
        self.assertEqual(expected, self.sol.MinimumDeleteSum(s1, s2))
    def test2(self):
        s1, s2 = 'delete', 'leet'
        expected = 403
        self.assertEqual(expected, self.sol.MinimumDeleteSum(s1, s2))

if __name__ == '__main__':
    unittest.main()
