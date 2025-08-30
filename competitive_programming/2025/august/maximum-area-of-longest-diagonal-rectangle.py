"""
Created Date: 2025-08-26
Qn: You are given a 2D 0-indexed integer array dimensions.

    For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents
    the length and dimensions[i][1] represents the width of the rectangle i.

    Return the area of the rectangle having the longest diagonal. If there are
    multiple rectangles with the longest diagonal, return the area of the
    rectangle having the maximum area.
Link: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
Notes:
"""

import math
import unittest
from functools import reduce


class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # functional approach
        # def max_diagonal_area(
        #     acc: tuple[float, int], dimension: list[int]
        # ) -> tuple[float, int]:
        #     max_diagonal, max_area = acc
        #     x, y = dimension
        #     cur_area = x * y
        #     cur_diagonal = math.sqrt(x**2 + y**2)
        #     if cur_diagonal > max_diagonal:
        #         max_diagonal = cur_diagonal
        #         max_area = x * y
        #     elif cur_diagonal == max_diagonal and cur_area > max_area:
        #         max_area = x * y
        #     return (max_diagonal, max_area)
        #
        # _, max_area = reduce(max_diagonal_area, dimensions, initial=(0, 0))
        # return max_area

        # Imperative approach
        diagonal = lambda x, y: math.sqrt(x**2 + y ** 2)
        max_diagonal = 0
        res = dimensions[0][0] * dimensions[0][1]
        for x, y in dimensions:
            cur_diagonal = diagonal(x, y)
            if cur_diagonal > max_diagonal:
                max_diagonal = cur_diagonal
                res = x * y
            elif cur_diagonal == max_diagonal and x * y > res:
                res = x * y
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_areaOfMaxDiagonal1(self):
        d = [[9, 3], [8, 6]]
        expected = 48
        self.assertEqual(expected, self.sol.areaOfMaxDiagonal(d))

    def test_areaOfMaxDiagonal2(self):
        d = [[3, 4], [4, 3]]
        expected = 12
        self.assertEqual(expected, self.sol.areaOfMaxDiagonal(d))


if __name__ == '__main__':
    unittest.main()
