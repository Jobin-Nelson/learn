"""
Created Date: 2024-11-24
Qn: You are given an n x n integer matrix. You can do the following operation
    any number of times:

    - Choose any two adjacent elements of matrix and multiply each of them by
      -1. Two elements are considered adjacent if and only if they share a
      border.

    Your goal is to maximize the summation of the matrix's elements. Return the
    maximum sum of the matrix's elements using the operation mentioned above.
Link: https://leetcode.com/problems/maximum-matrix-sum/
Notes:
    - get count of min elements
    - if it is even return absolute sum
    - if it is odd return absolute sum - (2 * absolute min)
"""

import unittest
from sys import maxsize


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        # functional approach
        def calc(x: tuple[int, int, int], y: int) -> tuple[int, int, int]:
            cur_sum, min_num, neg_count = x
            return (cur_sum + y, min(min_num, y), neg_count + 1 if y < 0 else neg_count)

        # Imperative approach
        # cur_sum = 0
        # neg_nums = 0
        # min_num = maxsize
        # for row in matrix:
        #     for e in row:
        #         abs_e = abs(e)
        #         cur_sum += abs_e
        #         min_num = min(min_num, abs_e)
        #         if e < 0:
        #             neg_nums += 1
        # return cur_sum - (2 * min_num) if neg_nums & 1 else cur_sum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxMatrixSum1(self):
        m = [[1, -1], [-1, 1]]
        self.assertEqual(self.sol.maxMatrixSum(m), 4)

    def test_maxMatrixSum2(self):
        m = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
        self.assertEqual(self.sol.maxMatrixSum(m), 16)


if __name__ == '__main__':
    unittest.main()
