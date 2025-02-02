"""
Created Date: 2025-01-28
Qn: You are given a 0-indexed 2D matrix grid of size m x n, where (r, c)
    represents:

    - A land cell if grid[r][c] = 0, or
    - A water cell containing grid[r][c] fish, if grid[r][c] > 0.

    A fisher can start at any water cell (r, c) and can do the following
    operations any number of times:

    - Catch all the fish at cell (r, c), or
    - Move to any adjacent water cell.

    Return the maximum number of fish the fisher can catch if he chooses his
    starting cell optimally, or 0 if no water cell exists.

    An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c
    - 1), (r + 1, c) or (r - 1, c) if it exists.
Link: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
Notes:
"""

import unittest


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r: int, c: int) -> int:
            fishes = grid[r][c]
            grid[r][c] = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0:
                    fishes += dfs(nr, nc)
            return fishes

        return max((dfs(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0), default=0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findMaxFish1(self):
        g = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
        expected = 7
        self.assertEqual(expected, self.sol.findMaxFish(g))

    def test_findMaxFish2(self):
        g = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        expected = 1
        self.assertEqual(expected, self.sol.findMaxFish(g))


if __name__ == '__main__':
    unittest.main()
