"""
Created Date: 2026-03-20
Qn: You are given an m x n integer matrix grid and an integer k.

    For every contiguous k x k submatrix of grid, compute the minimum absolute
    difference between any two distinct values within that submatrix.

    Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is
    the minimum absolute difference in the submatrix whose top-left corner is
    (i, j) in grid.

    Note: If all elements in the submatrix have the same value, the answer will
    be 0.

    A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all
    cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
Link: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
Notes:
    - use bruteforce
"""

import unittest
from itertools import pairwise


class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        R, C = len(grid), len(grid[0])
        res = [[0] * (C - k + 1) for _ in range(R - k + 1)]

        for r in range(R - k + 1):
            for c in range(C - k + 1):
                cur_stack = {grid[r + i][c + j] for i in range(k) for j in range(k)}
                sorted_stack = sorted(cur_stack)
                res[r][c] = min(
                    (abs(x - y) for x, y in pairwise(sorted_stack)), default=0
                )
        return res

        # Functional approach
        # return [
        #     [
        #         min(
        #             (
        #                 abs(x - y)
        #                 for x, y in pairwise(
        #                     sorted(
        #                         {grid[r + i][c + j] for i in range(k) for j in range(k)}
        #                     )
        #                 )
        #             ),
        #             default=0,
        #         )
        #         for c in range(C - k + 1)
        #     ]
        #     for r in range(R - k + 1)
        # ]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        grid = [[1, 8], [3, -2]]
        k = 2
        expected = [[2]]
        self.assertEqual(expected, self.sol.minAbsDiff(grid, k))

    def test2(self):
        grid = [[3, -1]]
        k = 1
        expected = [[0, 0]]
        self.assertEqual(expected, self.sol.minAbsDiff(grid, k))

    def test3(self):
        grid = [[1, -2, 3], [2, 3, 5]]
        k = 2
        expected = [[1, 2]]
        self.assertEqual(expected, self.sol.minAbsDiff(grid, k))


if __name__ == '__main__':
    unittest.main()
