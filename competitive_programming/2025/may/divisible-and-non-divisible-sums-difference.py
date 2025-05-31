"""
Created Date: 2025-05-27
Qn: You are given positive integers n and m.

    Define two integers as follows:

    - num1: The sum of all integers in the range [1, n] (both inclusive) that
      are not divisible by m.
    - num2: The sum of all integers in the range [1, n] (both inclusive) that
      are divisible by m.

    Return the integer num1 - num2.
Link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
Notes:
"""

import unittest
from operator import eq, ne
from typing import Callable


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        def count(op: Callable[[int, int], bool]) -> int:
            return sum(i for i in range(1, n + 1) if op(i % m, 0))

        return count(ne) - count(eq)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_differenceOfSums1(self):
        n, m = 10, 3
        expected = 19
        self.assertEqual(expected, self.sol.differenceOfSums(n, m))

    def test_differenceOfSums2(self):
        n, m = 5, 6
        expected = 15
        self.assertEqual(expected, self.sol.differenceOfSums(n, m))

    def test_differenceOfSums3(self):
        n, m = 5, 1
        expected = -15
        self.assertEqual(expected, self.sol.differenceOfSums(n, m))


if __name__ == '__main__':
    unittest.main()
