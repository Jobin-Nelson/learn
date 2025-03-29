"""
Created Date: 2025-03-28
Qn: You are given an m x n integer matrix grid and an array queries of size k.

    Find an array answer of size k such that for each integer queries[i] you
    start in the top left cell of the matrix and repeat the following process:

    - If queries[i] is strictly greater than the value of the current cell that
      you are in, then you get one point if it is your first time visiting this
      cell, and you can move to any adjacent cell in all 4 directions: up,
      down, left, and right.
    - Otherwise, you do not get any points, and you end this process.

    After the process, answer[i] is the maximum number of points you can get.
    Note that for each query you are allowed to visit the same cell multiple
    times.

    Return the resulting array answer.
Link: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
Notes:
    - sort the queries
    - use min heap with bfs
"""

import unittest
import heapq


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        R, C = len(grid), len(grid[0])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [0] * len(queries)
        points = 0

        h = [(grid[0][0], 0, 0)]
        grid[0][0] = 0
        for limit, index in sorted_queries:
            while h and h[0][0] < limit:
                _, r, c = heapq.heappop(h)
                points += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0:
                        heapq.heappush(h, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0
            res[index] = points

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxPoints1(self):
        g = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
        q = [5, 6, 2]
        expected = [5, 8, 1]
        self.assertEqual(expected, self.sol.maxPoints(g, q))

    def test_maxPoints2(self):
        g = [[5, 2, 1], [1, 1, 2]]
        q = [3]
        expected = [0]
        self.assertEqual(expected, self.sol.maxPoints(g, q))


if __name__ == '__main__':
    unittest.main()
