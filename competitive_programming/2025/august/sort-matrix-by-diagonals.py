"""
Created Date: 2025-08-28
Qn: You are given an n x n square matrix of integers grid. Return the matrix
    such that:

    - The diagonals in the bottom-left triangle (including the middle diagonal)
      are sorted in non-increasing order.
    - The diagonals in the top-right triangle are sorted in non-decreasing
      order.
Link: https://leetcode.com/problems/sort-matrix-by-diagonals/
Notes:
"""

import unittest


class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        R, C = len(grid), len(grid[0])

        # bottom left triangle
        for r in range(R):
            diagonal = [grid[j][i] for i, j in enumerate(range(r, R))]
            diagonal.sort(reverse=True)
            for  i, j in enumerate(range(r, C)):
                grid[j][i] = diagonal[i]

        # top right triangle
        for c in range(1, C):
            diagonal = [grid[i][j] for i, j in enumerate(range(c, C))]
            diagonal.sort()
            for  i, j in enumerate(range(c, C)):
                grid[i][j] = diagonal[i]
        return grid


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sortMatrix1(self):
        g = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
        expected = [[8, 2, 3], [9, 6, 7], [4, 5, 1]]
        self.assertEqual(expected, self.sol.sortMatrix(g))

    def test_sortMatrix2(self):
        g = [[0, 1], [1, 2]]
        expected = [[2, 1], [1, 0]]
        self.assertEqual(expected, self.sol.sortMatrix(g))

    def test_sortMatrix3(self):
        g = [[1]]
        expected = [[1]]
        self.assertEqual(expected, self.sol.sortMatrix(g))


if __name__ == '__main__':
    unittest.main()
