"""
Created Date: 2025-03-26
Qn: You are given a 2D integer grid of size m x n and an integer x. In one
    operation, you can add x to or subtract x from any element in the grid.

    A uni-value grid is a grid where all the elements of it are equal.

    Return the minimum number of operations to make the grid uni-value. If it
    is not possible, return -1.
Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
Notes:
    - use modulus to determine if it's possible to add or subtract x to same number
    - sort and count cost_left and cost_right
"""

import unittest


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        if any(n % x != grid[0][0] % x for row in grid for n in row):
            return -1

        nums = sorted([n for row in grid for n in row])
        total = sum(nums)
        prefix = 0
        N = len(nums)
        res = float('inf')

        for i, n in enumerate(nums):
            cost_left = n * i - prefix
            cost_right = total - prefix - (n * (N - i))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefix += n
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minOperations1(self):
        g = [[2, 4], [6, 8]]
        x = 2
        expected = 4
        self.assertEqual(expected, self.sol.minOperations(g, x))

    def test_minOperations2(self):
        g = [[1, 5], [2, 3]]
        x = 1
        expected = 5
        self.assertEqual(expected, self.sol.minOperations(g, x))

    def test_minOperations3(self):
        g = [[1, 2], [3, 4]]
        x = 2
        expected = -1
        self.assertEqual(expected, self.sol.minOperations(g, x))


if __name__ == '__main__':
    unittest.main()
