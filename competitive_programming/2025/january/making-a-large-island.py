"""
Created Date: 2025-01-31
Qn: You are given an n x n binary matrix grid. You are allowed to change at
    most one 0 to be 1.

    Return the size of the largest island in grid after applying this
    operation.

    An island is a 4-directionally connected group of 1s.
Link: https://leetcode.com/problems/making-a-large-island/
Notes:
    - use dfs
"""

import unittest
from collections import defaultdict


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r: int, c: int) -> bool:
            return r < 0 or r >= N or c < 0 or c >= N

        def dfs(r: int, c: int, label: int) -> int:
            grid[r][c] = label
            size = 1
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if out_of_bounds(nr, nc) or grid[nr][nc] != 1:
                    continue
                size += dfs(nr, nc, label)
            return size

        size = defaultdict(int)
        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        def connect(r: int, c: int) -> int:
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visit = set()

            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    res += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res

        return max(
            max(size.values(), default=0),
            max(
                (connect(r, c) for r in range(N) for c in range(N) if grid[r][c] == 0),
                default=0,
            ),
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestIsland1(self):
        g = [[1, 0], [0, 1]]
        expected = 3
        self.assertEqual(expected, self.sol.largestIsland(g))

    def test_largestIsland2(self):
        g = [[1, 1], [1, 0]]
        expected = 4
        self.assertEqual(expected, self.sol.largestIsland(g))

    def test_largestIsland3(self):
        g = [[1, 1], [1, 1]]
        expected = 4
        self.assertEqual(expected, self.sol.largestIsland(g))


if __name__ == '__main__':
    unittest.main()
