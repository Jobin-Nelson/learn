"""
Created Date: 2026-03-19
Qn: Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or
    '.', return the number of submatrices that contain:

    - grid[0][0]
    - an equal frequency of 'X' and 'Y'.
    - at least one 'X'.
Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
Notes:
"""

import unittest


class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        cols = [(0, 0)] * C

        for r in range(R):
            x = 0
            y = 0
            for c in range(C):
                cell = grid[r][c]
                if cell == 'X':
                    x += 1
                elif cell == 'Y':
                    y += 1
                cols[c] = cols[c][0] + x, cols[c][1] + y
                cum_x, cum_y = cols[c]
                if cum_x > 0 and cum_x == cum_y:
                    res += 1
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        g = [["X", "Y", "."], ["Y", ".", "."]]
        expected = 3
        self.assertEqual(expected, self.sol.numberOfSubmatrices(g))

    def test2(self):
        g = [["X", "X"], ["X", "Y"]]
        expected = 0
        self.assertEqual(expected, self.sol.numberOfSubmatrices(g))

    def test3(self):
        g = [[".", "."], [".", "."]]
        expected = 0
        self.assertEqual(expected, self.sol.numberOfSubmatrices(g))


if __name__ == '__main__':
    unittest.main()
