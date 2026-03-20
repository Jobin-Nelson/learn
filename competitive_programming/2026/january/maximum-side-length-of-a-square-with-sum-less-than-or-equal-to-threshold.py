"""
Created Date: 2026-01-19
Qn: Given a m x n matrix mat and an integer threshold, return the maximum
    side-length of a square with a sum less than or equal to threshold or
    return 0 if there is no such square.
Link: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
Notes:
"""

import unittest


class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        p = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                p[i][j] = (
                    p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + mat[i - 1][j - 1]
                )

        def get_rect_sum(x1: int, y1: int, x2: int, y2: int) -> int:
            return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]

        l, r = 1, min(m, n)
        res = 0
        while l <= r:
            mid = (l + r) >> 1
            find = any(
                get_rect_sum(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )
            if find:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
        t = 4
        expected = 2
        self.assertEqual(expected, self.sol.maxSideLength(m, t))

    def test2(self):
        m = [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
        ]
        t = 1
        expected = 0
        self.assertEqual(expected, self.sol.maxSideLength(m, t))


if __name__ == '__main__':
    unittest.main()
