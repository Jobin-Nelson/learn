"""
Created Date: 2024-11-29
Qn: You are given a m x n matrix grid consisting of non-negative integers where
    grid[row][col] represents the minimum time required to be able to visit the
    cell (row, col), which means you can visit the cell (row, col) only when
    the time you visit it is greater than or equal to grid[row][col].

    You are standing in the top-left cell of the matrix in the 0th second, and
    you must move to any adjacent cell in the four directions: up, down, left,
    and right. Each move you make takes 1 second.

    Return the minimum time required in which you can visit the bottom-right
    cell of the matrix. If you cannot visit the bottom-right cell, then return
    -1.
Link: https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
Notes:
    - use min heap
"""

import unittest
import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = [(0, 0, 0)]
        visit = set([(0, 0)])
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if (r, c) == (R - 1, C - 1):
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < R or not 0 <= nc < C or (nr, nc) in visit:
                    continue
                wait = 0
                if abs(grid[nr][nc] - t) & 1 == 0:
                    wait = 1
                next_time = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(min_heap, (next_time, nr, nc))
                visit.add((nr, nc))
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumTime1(self):
        g = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
        self.assertEqual(self.sol.minimumTime(g), 7)

    def test_minimumTime2(self):
        g = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
        self.assertEqual(self.sol.minimumTime(g), -1)


if __name__ == '__main__':
    unittest.main()
