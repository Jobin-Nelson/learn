"""
Created Date: 2025-08-30
Qn: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
    be validated according to the following rules:

    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
      without repetition.

    Note:

    - A Sudoku board (partially filled) could be valid but is not necessarily
      solvable.
    - Only the filled cells need to be validated according to the mentioned
      rules.
Link: https://leetcode.com/problems/valid-sudoku/
Notes:
"""

import unittest
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(n):
            for c in range(n):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in rows[r] or cell in cols[c] or cell in square[(r//3, c//3)]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                square[(r//3,c//3)].add(cell)

        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        b = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = True
        self.assertEqual(expected, self.sol.isValidSudoku(b))

    def test2(self):
        b = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        self.assertEqual(expected, self.sol.isValidSudoku(b))


if __name__ == '__main__':
    unittest.main()
