"""
Created Date: 2026-01-13
Qn: You are given a 2D integer array squares. Each squares[i] = [xi, yi, li]
    represents the coordinates of the bottom-left point and the side length of
    a square parallel to the x-axis.

    Find the minimum y-coordinate value of a horizontal line such that the
    total area of the squares above the line equals the total area of the
    squares below the line.

    Answers within 10-5 of the actual answer will be accepted.

    Note: Squares may overlap. Overlapping areas should be counted multiple
    times.
Link: https://leetcode.com/problems/separate-squares-i/
Notes:
"""

import unittest


class Solution:
    def seperateSquares(self, squares: list[list[int]]) -> float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2

        lo, hi = 0, max_y
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = [[0, 0, 1], [2, 2, 1]]
        expected = 1.0000
        self.assertAlmostEqual(expected, self.sol.seperateSquares(s), places=5)

    def test2(self):
        s = [[0, 0, 2], [1, 1, 1]]
        expected = 1.16667
        self.assertAlmostEqual(expected, self.sol.seperateSquares(s), places=5)


if __name__ == '__main__':
    unittest.main()
