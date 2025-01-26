"""
Created Date: 2025-01-22
Qn: You are given an integer matrix isWater of size m x n that represents a map
    of land and water cells.

    - If isWater[i][j] == 0, cell (i, j) is a land cell.
    - If isWater[i][j] == 1, cell (i, j) is a water cell. You must assign each
      cell a height in a way that follows these rules:

    The height of each cell must be non-negative.

    - If the cell is a water cell, its height must be 0.
    - Any two adjacent cells must have an absolute height difference of at most
      1.
    - A cell is adjacent to another cell if the former is directly north, east,
      south, or west of the latter (i.e., their sides are touching). Find an
      assignment of heights such that the maximum height in the matrix is
      maximized.

    Return an integer matrix height of size m x n where height[i][j] is cell
    (i, j)'s height. If there are multiple solutions, return any of them.

Link: https://leetcode.com/problems/map-of-highest-peak/
Notes:
    - use bfs
"""

import unittest
from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        R, C = len(isWater), len(isWater[0])
        q = deque()
        res = [[-1] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0

        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        while q:
            r, c = q.popleft()
            h = res[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr == R or nc == C or res[nr][nc] != -1:
                    continue
                q.append((nr, nc))
                res[nr][nc] = h + 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_highestPeak1(self):
        iw = [[0, 1], [0, 0]]
        expected = [[1, 0], [2, 1]]
        self.assertEqual(expected, self.sol.highestPeak(iw))

    def test_highestPeak2(self):
        iw = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
        expected = [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        self.assertEqual(expected, self.sol.highestPeak(iw))


if __name__ == '__main__':
    unittest.main()
