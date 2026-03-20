"""
Created Date: 2026-03-18
Qn: You are given a 0-indexed integer matrix grid and an integer k.

    Return the number of submatrices that contain the top-left element of the
    grid, and have a sum less than or equal to k.
Link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
Notes:
"""

import unittest


class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        cols = [0] * C
        res = 0

        for r in range(R):
            row_sum = 0
            for c in range(C):
                cols[c] += grid[r][c]
                row_sum += cols[c]
                if row_sum > k:
                    break
                res += 1

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        g = [[7, 6, 3], [6, 6, 1]]
        k = 18
        expected = 4
        self.assertEqual(expected, self.sol.countSubmatrices(g, k))

    def test2(self):
        g = [[7, 2, 9], [1, 5, 0], [2, 6, 6]]
        k = 20
        expected = 6
        self.assertEqual(expected, self.sol.countSubmatrices(g, k))


if __name__ == '__main__':
    unittest.main()
