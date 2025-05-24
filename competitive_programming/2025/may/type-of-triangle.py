"""
Created Date: 2025-05-19
Qn: You are given a 0-indexed integer array nums of size 3 which can form the
    sides of a triangle.

    - A triangle is called equilateral if it has all sides of equal length.
    - A triangle is called isosceles if it has exactly two sides of equal
      length.
    - A triangle is called scalene if all its sides are of different lengths.

    Return a string representing the type of triangle that can be formed or
    "none" if it cannot form a triangle.
Link: https://leetcode.com/problems/type-of-triangle/
Notes:
"""

import unittest
from itertools import permutations


class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if any(a + b <= c for a, b, c in permutations(nums, 3)):
            return 'none'
        unique_sides = set(nums)
        if len(unique_sides) == 1:
            return 'equilateral'
        elif len(unique_sides) == 2:
            return 'isosceles'
        else:
            return 'scalene'


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_triangleType1(self):
        n = [3, 3, 3]
        expected = 'equilateral'
        self.assertEqual(expected, self.sol.triangleType(n))

    def test_triangleType2(self):
        n = [3, 4, 5]
        expected = 'scalene'
        self.assertEqual(expected, self.sol.triangleType(n))


if __name__ == '__main__':
    unittest.main()
