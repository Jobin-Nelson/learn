"""
Created Date: 2025-08-25
Qn: Given an m x n matrix mat, return an array of all the elements of the array
    in a diagonal order.
Link: https://leetcode.com/problems/diagonal-traverse/
Notes:
    - traverse top right direction then change direction
    - traverse bottom left direction then change direction
"""

import unittest


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # [
        # (0, 0),
        # (0, 1), (1, 0),
        # (2, 0), (1, 1), (0, 2)
        # (1, 2), (2, 1),
        # (2, 2)
        # ]
        r = c = 0
        R, C = len(mat), len(mat[0])

        res = [mat[0][0]]
        while r < R - 1 or c < C - 1:
            # top right direction
            while 0 <= (r - 1) < R and 0 <= (c + 1) < C:
                r -= 1
                c += 1
                res.append(mat[r][c])
            if c + 1 < C:
                c += 1
                res.append(mat[r][c])
            elif r + 1 < R:
                r += 1
                res.append(mat[r][c])

            # bottom left direction
            while 0 <= (r + 1) < R and 0 <= (c - 1) < C:
                r += 1
                c -= 1
                res.append(mat[r][c])
            if r + 1 < R:
                r += 1
                res.append(mat[r][c])
            elif c + 1 < C:
                c += 1
                res.append(mat[r][c])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findDiagonalOrder1(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
        self.assertEqual(expected, self.sol.findDiagonalOrder(mat))

    def test_findDiagonalOrder2(self):
        mat = [[1, 2], [3, 4]]
        expected = list(range(1, 5))
        self.assertEqual(expected, self.sol.findDiagonalOrder(mat))

    def test_findDiagonalOrder3(self):
        mat = [[2, 3]]
        expected = [2, 3]
        self.assertEqual(expected, self.sol.findDiagonalOrder(mat))


if __name__ == '__main__':
    unittest.main()
