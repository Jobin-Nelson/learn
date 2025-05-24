"""
Created Date: 2025-05-21
Qn: Given an m x n integer matrix matrix, if an element is 0, set its entire
    row and column to 0's.

    You must do it in place.
Link: https://leetcode.com/problems/set-matrix-zeroes/
Notes:
"""

import unittest


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in rows:
            matrix[r] = [0] * C
        for c in cols:
            for r in range(R):
                matrix[r][c] = 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_setZeroes1(self):
        m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.sol.setZeroes(m)
        self.assertEqual(expected, m)

    def test_setZeroes2(self):
        m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.sol.setZeroes(m)
        self.assertEqual(expected, m)


if __name__ == '__main__':
    unittest.main()
