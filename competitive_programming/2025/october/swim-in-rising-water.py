"""
Created Date: 2025-10-06
Qn: You are given an n x n integer matrix grid where each value grid[i][j]
    represents the elevation at that point (i, j).

    It starts raining, and water gradually rises over time. At time t, the
    water level is t, meaning any cell with elevation less than equal to t is
    submerged or reachable.

    You can swim from a square to another 4-directionally adjacent square if
    and only if the elevation of both squares individually are at most t. You
    can swim infinite distances in zero time. Of course, you must stay within
    the boundaries of the grid during your swim.

    Return the minimum time until you can reach the bottom right square (n - 1,
    n - 1) if you start at the top left square (0, 0).
Link: https://leetcode.com/problems/swim-in-rising-water/
Notes:
"""

import heapq
import unittest


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            h, r, c = heapq.heappop(q)
            if r == R - 1 and c == C - 1:
                return h
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(q, (max(h, grid[nr][nc]), nr, nc))
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = [[0, 2], [1, 3]]
        expected = 3
        self.assertEqual(expected, self.sol.swimInWater(m))

    def test2(self):
        m = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        expected = 16
        self.assertEqual(expected, self.sol.swimInWater(m))


if __name__ == '__main__':
    unittest.main()
