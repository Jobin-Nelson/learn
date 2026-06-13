"""
Created Date: 2026-05-04
Qn: You are given an n x n 2D matrix representing an image, rotate the image by
    90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the
    rotation.
Link: https://leetcode.com/problems/rotate-image/
Notes:
"""

import unittest


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topleft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topleft
            l += 1
            r -= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.sol.rotate(m)
        self.assertEqual(expected, m)

    def test2(self):
        m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.sol.rotate(m)
        self.assertEqual(expected, m)


if __name__ == '__main__':
    unittest.main()
