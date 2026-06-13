"""
Created Date: 2026-03-22
Qn: Given two n x n binary matrices mat and target, return true if it is
    possible to make mat equal to target by rotating mat in 90-degree
    increments, or false otherwise.
Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
Notes:
    - rotate 4 times and check
"""

import unittest


class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        N = len(mat)

        def rotate_90(g: list[list[int]]) -> list[list[int]]:
            nonlocal N
            return [[g[N - 1 - i][j] for i in range(N)] for j in range(N)]

        res = mat
        for _ in range(4):
            res = rotate_90(res)
            if res == target:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = [[0, 1], [1, 0]]
        t = [[1, 0], [0, 1]]
        expected = True
        self.assertEqual(expected, self.sol.findRotation(m, t))

    def test2(self):
        m = [[0, 1], [1, 1]]
        t = [[1, 0], [0, 1]]
        expected = False
        self.assertEqual(expected, self.sol.findRotation(m, t))

    def test3(self):
        m = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        t = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        expected = True
        self.assertEqual(expected, self.sol.findRotation(m, t))


if __name__ == '__main__':
    unittest.main()
