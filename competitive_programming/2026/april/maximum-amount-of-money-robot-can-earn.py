"""
Created Date: 2026-04-02
Qn: You are given an m x n grid. A robot starts at the top-left corner of the
    grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The
    robot can move either right or down at any point in time.

    The grid contains a value coins[i][j] in each cell:

    If coins[i][j] >= 0, the robot gains that many coins. If coins[i][j] < 0,
    the robot encounters a robber, and the robber steals the absolute value of
    coins[i][j] coins. The robot has a special ability to neutralize robbers in
    at most 2 cells on its path, preventing them from stealing coins in those
    cells.

    Note: The robot's total coins can be negative.

    Return the maximum profit the robot can gain on the route. Link:
https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
Notes:
    - use dp
"""

import unittest
from sys import maxsize


class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        n = len(coins[0])
        dp = [[-maxsize] * 3 for _ in range(n + 1)]
        dp[1] = [0] * 3
        for row in coins:
            for j, x in enumerate(row):
                dp[j + 1][2] = max(
                    dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1]
                )
                dp[j + 1][1] = max(
                    dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0]
                )
                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x
        return dp[n][2]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        coins = [[0, 1, -1], [1, -2, 3], [2, -3, 4]]
        expected = 8
        self.assertEqual(expected, self.sol.maximumAmount(coins))

    def test2(self):
        coins = [[10, 10, 10], [10, 10, 10]]
        expected = 40
        self.assertEqual(expected, self.sol.maximumAmount(coins))


if __name__ == '__main__':
    unittest.main()
