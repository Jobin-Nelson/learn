"""
Created Date: 2025-05-18
Qn: You are given two integers m and n. Consider an m x n grid where each cell
    is initially white. You can paint each cell red, green, or blue. All cells
    must be painted.

    Return the number of ways to color the grid with no two adjacent cells
    having the same color. Since the answer can be very large, return it modulo
    109 + 7.
Link: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
Notes:
    - use bitmasking and dp
"""

import unittest


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        dp = [[-1] * 1024 for _ in range(1002)]

        def count_ways(r: int, c: int, curr_state: int, prev_state: int) -> int:
            if c == n:
                return 1
            if r == m:
                return count_ways(0, c + 1, 0, curr_state)
            if r == 0 and dp[c][prev_state] != -1:
                return dp[c][prev_state]

            up_color = curr_state & 3 if r > 0 else 0
            left_color = (prev_state >> ((m - r - 1) * 2)) & 3

            ways_to_color = 0
            for color in range(1, 4):
                if color != up_color and color != left_color:
                    ways_to_color = (
                        ways_to_color
                        + count_ways(r + 1, c, (curr_state << 2) + color, prev_state)
                    ) % mod
            if r == 0:
                dp[c][prev_state] = ways_to_color
            return ways_to_color

        return count_ways(0, 0, 0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_colorTheGrid1(self):
        m, n = 1, 1
        expected = 3
        self.assertEqual(expected, self.sol.colorTheGrid(m, n))

    def test_colorTheGrid2(self):
        m, n = 1, 2
        expected = 6
        self.assertEqual(expected, self.sol.colorTheGrid(m, n))

    def test_colorTheGrid3(self):
        m, n = 5, 5
        expected = 580986
        self.assertEqual(expected, self.sol.colorTheGrid(m, n))


if __name__ == '__main__':
    unittest.main()
