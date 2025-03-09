"""
Created Date: 2025-03-05
Qn:There exists an infinitely large two-dimensional grid of uncolored unit
    cells. You are given a positive integer n, indicating that you must do the
    following routine for n minutes:

    - At the first minute, color any arbitrary unit cell blue.
    - Every minute thereafter, color blue every uncolored cell that touches a
      blue cell.

    Below is a pictorial representation of the state of the grid after minutes
    1, 2, and 3.
Link: https://leetcode.com/problems/count-total-number-of-colored-cells/
Notes:
    - at each iteration 4 more cells are added
    - 1 + 4 * ((n) * (n-1)) / 2
    - 1 + n * (n - 1) * 2
"""

import unittest


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_coloredCells1(self):
        n = 1
        expected = 1
        self.assertEqual(expected, self.sol.coloredCells(n))

    def test_coloredCells2(self):
        n = 2
        expected = 5
        self.assertEqual(expected, self.sol.coloredCells(n))


if __name__ == '__main__':
    unittest.main()
