"""
Created Date: 2025-01-18
Qn: Given an m x n grid. Each cell of the grid has a sign pointing to the next
    cell you should visit if you are currently in this cell. The sign of
    grid[i][j] can be:

    - 1 which means go to the cell to the right. (i.e go from grid[i][j] to
      grid[i][j + 1])
    - 2 which means go to the cell to the left. (i.e go from grid[i][j] to
      grid[i][j - 1])
    - 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
      1][j])
    - 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
      1][j])

    Notice that there could be some signs on the cells of the grid that point
    outside the grid.

    You will initially start at the upper left cell (0, 0). A valid path in the
    grid is a path that starts from the upper left cell (0, 0) and ends at the
    bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
    path does not have to be the shortest.

    You can modify the sign on a cell with cost = 1. You can modify the sign on
    a cell one time only.

    Return the minimum cost to make the grid have at least one valid path.
Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
Notes:
    - use bfs
"""

import unittest
from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])
        min_cost = {(0, 0): 0}

        while q:
            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost
            for d, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1
                if (
                    nr < 0
                    or nc < 0
                    or nr == ROWS
                    or nc == COLS
                    or n_cost >= min_cost.get((nr, nc), float('inf'))
                ):
                    continue
                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minCost1(self):
        g = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
        expected = 3
        self.assertEqual(expected, self.sol.minCost(g))

    def test_minCost2(self):
        g = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
        expected = 0
        self.assertEqual(expected, self.sol.minCost(g))

    def test_minCost3(self):
        g = [[1, 2], [4, 3]]
        expected = 1
        self.assertEqual(expected, self.sol.minCost(g))


if __name__ == '__main__':
    unittest.main()
