"""
Created Date: 2025-08-15
Qn: Given an integer n, return true if it is a power of four. Otherwise, return
    false.

    An integer n is a power of four, if there exists an integer x such that n ==
    4x.
Link: https://leetcode.com/problems/power-of-four/
Notes:
"""

import unittest


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0 and n % 4 == 0:
            n //= 4
        return n == 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isPowerOfFour1(self):
        n = 16
        expected = True
        self.assertEqual(expected, self.sol.isPowerOfFour(n))

    def test_isPowerOfFour2(self):
        n = 5
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfFour(n))

    def test_isPowerOfFour3(self):
        n = 1
        expected = True
        self.assertEqual(expected, self.sol.isPowerOfFour(n))


if __name__ == '__main__':
    unittest.main()
