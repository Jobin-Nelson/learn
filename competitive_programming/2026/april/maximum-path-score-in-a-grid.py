"""
Created Date: 2026-04-30
Qn: You are given an m x n grid where each cell contains one of the values 0,
    1, or 2. You are also given an integer k.

    You start from the top-left corner (0, 0) and want to reach the
    bottom-right corner (m - 1, n - 1) by moving only right or down.

    Each cell contributes a specific score and incurs an associated cost,
    according to their cell values:

    - 0: adds 0 to your score and costs 0.
    - 1: adds 1 to your score and costs 1.
    - 2: adds 2 to your score and costs 1.

    Return the maximum score achievable without exceeding a total cost of k, or
    -1 if no valid path exists.

    Note: If you reach the last cell but the total cost exceeds k, the path is
    invalid.
Link: https://leetcode.com/problems/maximum-path-score-in-a-grid/
Notes:
"""

import unittest


class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        inf = float('-inf')

        dp = [[[inf] * (k + 1) for _ in range(C)] for _ in range(R)]
        dp[0][0][0] = 0

        for i in range(R):
            for j in range(C):
                for c in range(k + 1):
                    if dp[i][j][c] == inf:
                        continue
                    if i + 1 < R:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        cur_cost = c + cost
                        if cur_cost <= k:
                            dp[i + 1][j][cur_cost] = max(
                                dp[i + 1][j][cur_cost], dp[i][j][c] + val
                            )
                    if j + 1 < C:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        cur_cost = c + cost
                        if cur_cost <= k:
                            dp[i][j + 1][cur_cost] = max(
                                dp[i][j + 1][cur_cost], dp[i][j][c] + val
                            )
        res = max(dp[R - 1][C - 1])
        return max(res, -1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        g, k = [[0, 1], [2, 0]], 1
        expected = 2
        self.assertEqual(expected, self.sol.maxPathScore(g, k))

    def test2(self):
        g, k = [[0, 1], [1, 2]], 1
        expected = -1
        self.assertEqual(expected, self.sol.maxPathScore(g, k))


if __name__ == '__main__':
    unittest.main()
