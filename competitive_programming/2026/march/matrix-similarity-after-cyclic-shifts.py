"""
Created Date: 2026-03-27
Qn: You are given an m x n integer matrix mat and an integer k. The matrix rows
    are 0-indexed.

    The following proccess happens k times:

    - Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
    - Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.

    Return true if the final modified matrix after k steps is identical to the
    original matrix, and false otherwise.
Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
Notes:
    - shift in one go and compare
"""

import unittest


class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        R, C = len(mat), len(mat[0])

        return not any(
            mat[r][c] != mat[r][(c + k) % C] for r in range(R) for c in range(C)
        )

        # Simulation
        # def shift(g: list[list[int]]) -> list[list[int]]:
        #     return [
        #         [row[-1]] + row[:-1] if i & 1 else row[1:] + [row[0]]
        #         for i, row in enumerate(g)
        #     ]
        #
        # shifted_mat = mat
        # for _ in range(k):
        #     shifted_mat = shift(shifted_mat)
        # return shifted_mat == mat


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m, k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4
        expected = False
        self.assertEqual(expected, self.sol.areSimilar(m, k))

    def test2(self):
        m, k = [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2
        expected = True
        self.assertEqual(expected, self.sol.areSimilar(m, k))

    def test3(self):
        m, k = [[2, 2], [2, 2]], 3
        expected = True
        self.assertEqual(expected, self.sol.areSimilar(m, k))


if __name__ == '__main__':
    unittest.main()
