"""
Created Date: 2024-11-22
Qn: You are given an m x n binary matrix matrix.

    You can choose any number of columns in the matrix and flip every cell in
    that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

    Return the maximum number of rows that have all values equal after some
    number of flips.
Link: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
Notes:
    - use pattern
    - there are 2 scenarios when two rows are equal
    - when each values are equal
    - when each values are opposite of the corresponding value in the other row
    - so what we are looking for is a pattern and not the number itself
"""

import unittest


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count = {}
        for row in matrix:
            pattern = "".join("T" if col == row[0] else "F" for col in row)
            count[pattern] = 1 + count.get(pattern, 0)
        return max(count.values(), default=0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxEqualRowsAfterFlips1(self):
        m = [[0, 1], [1, 1]]
        self.assertEqual(self.sol.maxEqualRowsAfterFlips(m), 1)

    def test_maxEqualRowsAfterFlips2(self):
        m = [[0, 1], [1, 0]]
        self.assertEqual(self.sol.maxEqualRowsAfterFlips(m), 2)

    def test_maxEqualRowsAfterFlips3(self):
        m = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
        self.assertEqual(self.sol.maxEqualRowsAfterFlips(m), 2)


if __name__ == '__main__':
    unittest.main()
