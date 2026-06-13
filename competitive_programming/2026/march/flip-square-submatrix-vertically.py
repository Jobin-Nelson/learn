"""
Created Date: 2026-03-21
Qn: You are given an m x n integer matrix grid, and three integers x, y, and k.

    The integers x and y represent the row and column indices of the top-left
    corner of a square submatrix and the integer k represents the size (side
    length) of the square submatrix.

    Your task is to flip the submatrix by reversing the order of its rows
    vertically.

    Return the updated matrix.
Link: https://leetcode.com/problems/flip-square-submatrix-vertically/
Notes:
    - use simulation
"""

import unittest


class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        for i in range(k):
            for j in range(k >> 1):
                r, c = x + j, y + i
                rx, cx = x + k - j - 1, c
                grid[r][c], grid[rx][cx] = grid[rx][cx], grid[r][c]
        return grid


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        g = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        x, y, k = 1, 0, 3
        expected = [[1, 2, 3, 4], [13, 14, 15, 8], [9, 10, 11, 12], [5, 6, 7, 16]]
        self.assertEqual(expected, self.sol.reverseSubmatrix(g, x, y, k))

    def test2(self):
        g = [[3, 4, 2, 3], [2, 3, 4, 2]]
        x, y, k = 0, 2, 2
        expected = [[3, 4, 4, 2], [2, 3, 2, 3]]
        self.assertEqual(expected, self.sol.reverseSubmatrix(g, x, y, k))


if __name__ == '__main__':
    unittest.main()
