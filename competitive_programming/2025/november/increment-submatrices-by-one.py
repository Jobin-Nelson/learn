"""
Created Date: 2025-11-14
Qn: You are given a positive integer n, indicating that we initially have an n
    x n 0-indexed integer matrix mat filled with zeroes.

    You are also given a 2D integer array query. For each query[i] = [row1i,
    col1i, row2i, col2i], you should do the following operation:

    Add 1 to every element in the submatrix with the top left corner (row1i,
    col1i) and the bottom right corner (row2i, col2i). That is, add 1 to
    mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i. Return the
    matrix mat after performing every query.
Link: https://leetcode.com/problems/increment-submatrices-by-one/
Notes:
    - use prefix sum
"""

import unittest


class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2 + 1][c2 + 1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1

        res = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else res[r - 1][c]
                left = 0 if c == 0 else res[r][c - 1]
                topleft = 0 if r == 0 or c == 0 else res[r - 1][c - 1]
                res[r][c] = diff[r][c] + top + left - topleft
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 3
        q = [[1, 1, 2, 2], [0, 0, 1, 1]]
        expected = [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
        self.assertEqual(expected, self.sol.rangeAddQueries(n, q))

    def test2(self):
        n = 2
        q = [[0, 0, 1, 1]]
        expected = [[1, 1], [1, 1]]
        self.assertEqual(expected, self.sol.rangeAddQueries(n, q))


if __name__ == '__main__':
    unittest.main()
