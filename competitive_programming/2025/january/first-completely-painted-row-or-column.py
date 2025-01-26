"""
Created Date: 2025-01-20
Qn: You are given a 0-indexed integer array arr, and an m x n integer matrix
    mat. arr and mat both contain all the integers in the range [1, m * n].

    Go through each index i in arr starting from index 0 and paint the cell in
    mat containing the integer arr[i].

    Return the smallest index i at which either a row or a column will be
    completely painted in mat.
Link: https://leetcode.com/problems/first-completely-painted-row-or-column/
Notes:
    - use hashmap to store mat nums to position
    - use list to store the painted rows and cols
"""

import unittest


class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        R, C = len(mat), len(mat[0])
        row_count, col_count = [0] * R, [0] * C
        num_to_pos = {mat[r][c]: (r, c) for r in range(R) for c in range(C)}

        for i, n in enumerate(arr):
            r, c = num_to_pos[n]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == C or col_count[c] == R:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_firstCompleteIndex1(self):
        a = [1, 3, 4, 2]
        m = [[1, 4], [2, 3]]
        expected = 2
        self.assertEqual(expected, self.sol.firstCompleteIndex(a, m))

    def test_firstCompleteIndex2(self):
        a = [2, 8, 7, 4, 1, 3, 5, 6, 9]
        m = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
        expected = 3
        self.assertEqual(expected, self.sol.firstCompleteIndex(a, m))


if __name__ == '__main__':
    unittest.main()
