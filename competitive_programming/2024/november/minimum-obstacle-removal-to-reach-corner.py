"""
Created Date: 2024-11-28
Qn: You are given a 0-indexed 2D integer array grid of size m x n. Each
    cell has one of two values:

    - 0 represents an empty cell,
    - 1 represents an obstacle that may be removed.

    You can move up, down, left, or right from and to an empty cell.

    Return the minimum number of obstacles to remove so you can move
    from the upper left corner (0, 0) to the lower right corner (m - 1,
    n - 1).
Link: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
Notes:
    - use deque or djikstra's
"""

import unittest
from sys import maxsize
from collections import deque


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_obstacles = [[maxsize] * C for _ in range(R)]
        min_obstacles[0][0] = 0

        q = deque([(0, 0, 0)])
        while q:
            obstacles, row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    not 0 <= nr < R
                    or not 0 <= nc < C
                    or min_obstacles[nr][nc] != maxsize
                ):
                    continue
                new_obstacles = obstacles
                if grid[nr][nc] == 1:
                    new_obstacles += 1
                    q.append((new_obstacles, nr, nc))
                else:
                    q.appendleft((new_obstacles, nr, nc))
                min_obstacles[nr][nc] = new_obstacles
        return min_obstacles[R - 1][C - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumObstacles1(self):
        g = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(self.sol.minimumObstacles(g), 2)

    def test_minimumObstacles2(self):
        g = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
        self.assertEqual(self.sol.minimumObstacles(g), 0)


if __name__ == '__main__':
    unittest.main()
