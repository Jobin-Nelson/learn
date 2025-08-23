"""
Created Date: 2025-08-21
Qn: Given an m x n binary matrix mat, return the number of submatrices that
    have all ones.
Link: https://leetcode.com/problems/count-submatrices-with-all-ones/
Notes:
    - use monotonic stack
"""

import unittest


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        heights = [0] * len(mat[0])
        res = 0
        for row in mat:
            for i, x in enumerate(row):
                heights[i] = 0 if x == 0 else heights[i] + 1
            stack = [[-1, 0, -1]]
            for i, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                j, prev, _ = stack[-1]
                cur = prev + (i-j) * h
                stack.append([i, cur, h])
                res += cur
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numSumat1(self):
        m = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
        expected = 13
        self.assertEqual(expected, self.sol.numSubmat(m))

    def test_numSumat2(self):
        m = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
        expected = 24
        self.assertEqual(expected, self.sol.numSubmat(m))


if __name__ == '__main__':
    unittest.main()
