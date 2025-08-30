"""
Created Date: 2025-08-27
Qn: You are given a 2D integer matrix grid of size n x m, where each element is
    either 0, 1, or 2.

    A V-shaped diagonal segment is defined as:

    - The segment starts with 1.
    - The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
    - The segment:
        - Starts along a diagonal direction (top-left to bottom-right, bottom-right
          to top-left, top-right to bottom-left, or bottom-left to top-right).
        - Continues the sequence in the same diagonal direction.
        - Makes at most one clockwise 90-degree turn to another diagonal direction
          while maintaining the sequence.

    Return the length of the longest V-shaped diagonal segment. If no valid
    segment exists, return 0.
Link: https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
Notes:
    - use dfs, use arguments
        - row, col
        - direction
        - turned or not
        - target
"""

import unittest
from functools import cache


class Solution:
    def lenOfDiagonal(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @cache
        def dfs(r: int, c: int, direction: int, turned: bool, target: int) -> int:
            res = 0
            dr, dc = dirs[direction]
            nr, nc = r + dr, c + dc
            new_target = target ^ 2
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == target:
                res = max(res, dfs(nr, nc, direction, turned, new_target))

            if not turned:
                new_dir = (direction + 1) % 4
                dr, dc = dirs[new_dir]
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == target:
                    res = max(res, dfs(nr, nc, new_dir, True, new_target))
            return res + 1

        return max(
            (
                dfs(r, c, d, False, 2)
                for r in range(R)
                for c in range(C)
                if grid[r][c] == 1
                for d in range(4)
            ),
            default=0,
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lenOfDiagonal1(self):
        g = [
            [2, 2, 1, 2, 2],
            [2, 0, 2, 2, 0],
            [2, 0, 1, 1, 0],
            [1, 0, 2, 2, 2],
            [2, 0, 0, 2, 2],
        ]
        expected = 5
        self.assertEqual(expected, self.sol.lenOfDiagonal(g))

    def test_lenOfDiagonal2(self):
        g = [
            [2, 2, 2, 2, 2],
            [2, 0, 2, 2, 0],
            [2, 0, 1, 1, 0],
            [1, 0, 2, 2, 2],
            [2, 0, 0, 2, 2],
        ]
        expected = 4
        self.assertEqual(expected, self.sol.lenOfDiagonal(g))

    def test_lenOfDiagonal3(self):
        g = [
            [1, 2, 2, 2, 2],
            [2, 2, 2, 2, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 2, 2, 2],
            [2, 0, 0, 2, 0],
        ]
        expected = 5
        self.assertEqual(expected, self.sol.lenOfDiagonal(g))

    def test_lenOfDiagonal4(self):
        g = [[1]]
        expected = 1
        self.assertEqual(expected, self.sol.lenOfDiagonal(g))


if __name__ == '__main__':
    unittest.main()
