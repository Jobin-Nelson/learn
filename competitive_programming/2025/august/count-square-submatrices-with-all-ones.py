"""
Created Date: 2025-08-20
Qn: Give a `m * n` matrix of ones and zeroes, return how many square
    submatrices have all ones
Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
Notes:
    - use dp
    - maximum possible square you can form for a given cell is 1 + min of i-1 j-1, i j-1, i-1 j
"""

import unittest


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev = matrix[0]
        res = sum(prev)
        for i in range(1, m):
            cur = [0] * n
            cur[0] = matrix[i][0]
            res += cur[0]
            for j in range(1, n):
                if matrix[i][j] == 1:
                    cur[j] = 1 + min(cur[j-1], prev[j-1], prev[j])
                    res += cur[j]
            prev = cur
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSquares1(self):
        m = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
        expected = 15
        self.assertEqual(expected, self.sol.countSquares(m))

    def test_countSquares2(self):
        m = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
        expected = 7
        self.assertEqual(expected, self.sol.countSquares(m))


if __name__ == '__main__':
    unittest.main()
