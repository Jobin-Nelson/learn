"""
Created Date: 2025-02-01
Qn: An array is considered special if every pair of its adjacent elements
    contains two numbers with different parity.

    You are given an array of integers nums. Return true if nums is a special
    array, otherwise, return false.
Link: https://leetcode.com/problems/special-array-i/
Notes:
"""

import unittest
from itertools import pairwise
from operator import ne



class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        psi = lambda f, g: lambda x,y: f(g(x), g(y))
        is_odd = lambda x: x & 1
        return all(map(psi(ne,is_odd), nums, nums[1:]))
        # return all((a & 1) != (b & 1) for a, b in pairwise(nums))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isArraySpecial1(self):
        n = [1]
        expected = True
        self.assertEqual(expected, self.sol.isArraySpecial(n))

    def test_isArraySpecial2(self):
        n = [2, 1, 4]
        expected = True
        self.assertEqual(expected, self.sol.isArraySpecial(n))

    def test_isArraySpecial3(self):
        n = [4, 3, 1, 6]
        expected = False
        self.assertEqual(expected, self.sol.isArraySpecial(n))


if __name__ == '__main__':
    unittest.main()
