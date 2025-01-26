"""
Created Date: 2025-01-21
Qn: You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c]
    represents the number of points at position (r, c) on the matrix. Two
    robots are playing a game on this matrix.

    Both robots initially start at (0, 0) and want to reach (1, n-1). Each
    robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to
    (r + 1, c)).

    At the start of the game, the first robot moves from (0, 0) to (1, n-1),
    collecting all the points from the cells on its path. For all cells (r, c)
    traversed on the path, grid[r][c] is set to 0. Then, the second robot moves
    from (0, 0) to (1, n-1), collecting the points on its path. Note that their
    paths may intersect with one another.

    The first robot wants to minimize the number of points collected by the
    second robot. In contrast, the second robot wants to maximize the number of
    points it collects. If both robots play optimally, return the number of
    points collected by the second robot.
Link: https://leetcode.com/problems/grid-game/
Notes:
    - turn index and find the minimum sum
"""

import unittest
from sys import maxsize
from itertools import accumulate, islice
from operator import neg


class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        # Functional approach
        first_row = islice(accumulate(map(neg, grid[0]), initial=sum(grid[0])), 1, None)
        second_row = accumulate(grid[1], initial=0)
        return min(map(max, first_row, second_row))

        # Imperative approach
        # first_row_sum = sum(grid[0])
        # second_row_sum = 0
        # minimum_sum = maxsize
        #
        # for turn_index in range(len(grid[0])):
        #     first_row_sum -= grid[0][turn_index]
        #     minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
        #     second_row_sum += grid[1][turn_index]
        # return minimum_sum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_gridGame1(self):
        g = [[2, 5, 4], [1, 5, 1]]
        expected = 4
        self.assertEqual(expected, self.sol.gridGame(g))

    def test_gridGame2(self):
        g = [[3, 3, 1], [8, 5, 2]]
        expected = 4
        self.assertEqual(expected, self.sol.gridGame(g))

    def test_gridGame3(self):
        g = [[1, 3, 1, 15], [1, 3, 3, 1]]
        expected = 7
        self.assertEqual(expected, self.sol.gridGame(g))


if __name__ == '__main__':
    unittest.main()
