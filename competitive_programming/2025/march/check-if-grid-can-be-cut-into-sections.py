"""
Created Date: 2025-03-25
Qn: You are given an integer n representing the dimensions of an n x n grid,
    with the origin at the bottom-left corner of the grid. You are also given a
    2D array of coordinates rectangles, where rectangles[i] is in the form
    [startx, starty, endx, endy], representing a rectangle on the grid. Each
    rectangle is defined as follows:

    - (startx, starty): The bottom-left corner of the rectangle.
    - (endx, endy): The top-right corner of the rectangle.

    Note that the rectangles do not overlap. Your task is to determine if it is
    possible to make either two horizontal or two vertical cuts on the grid
    such that:

    - Each of the three resulting sections formed by the cuts contains at least
      one rectangle.
    - Every rectangle belongs to exactly one section.

    Return true if such cuts can be made; otherwise, return false.
Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
Notes:
    - use sorted intervals
"""

import unittest
from itertools import accumulate


class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x = sorted([(r[0], r[2]) for r in rectangles])
        y = sorted([(r[1], r[3]) for r in rectangles])

        def count(acc: tuple[int, int], interval: tuple[int, int]) -> tuple[int, int]:
            length, latest_end = acc
            start, end = interval
            return (
                (length + 1, end)
                if start >= latest_end
                else (length, max(end, latest_end))
            )

        def isDividableTwice(intervals: list[tuple[int, int]]) -> bool:
            return any(c[0] >= 3 for c in accumulate(intervals, count, initial=(0, 0)))

        return isDividableTwice(x) or isDividableTwice(y)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_checkValidCuts1(self):
        n = 5
        r = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
        expected = True
        self.assertEqual(expected, self.sol.checkValidCuts(n, r))

    def test_checkValidCuts2(self):
        n = 4
        r = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
        expected = True
        self.assertEqual(expected, self.sol.checkValidCuts(n, r))

    def test_checkValidCuts3(self):
        n = 4
        r = [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]
        expected = False
        self.assertEqual(expected, self.sol.checkValidCuts(n, r))

    def test_checkValidCuts4(self):
        n = 4
        r = [[0, 0, 1, 4], [1, 0, 2, 3], [2, 0, 3, 3], [3, 0, 4, 3], [1, 3, 4, 4]]
        expected = False
        self.assertEqual(expected, self.sol.checkValidCuts(n, r))


if __name__ == '__main__':
    unittest.main()
