"""
Created Date: 2025-08-09
Qn: Given an integer n, return true if it is a power of two. Otherwise, return
    false.

    An integer n is a power of two, if there exists an integer x such that n == 2x.
Link: https://leetcode.com/problems/power-of-two/
Notes:
    - has to be positive
    - the number should be only with one bit for it to be a power of two
"""

import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isPowerOfTwo1(self):
        n = 1
        expected = True
        self.assertEqual(expected, self.sol.isPowerOfTwo(n))

    def test_isPowerOfTwo2(self):
        n = 16
        expected = True
        self.assertEqual(expected, self.sol.isPowerOfTwo(n))

    def test_isPowerOfTwo3(self):
        n = 3
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfTwo(n))

    def test_isPowerOfTwo4(self):
        n = 6
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfTwo(n))

    def test_isPowerOfTwo5(self):
        n = -16
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfTwo(n))


if __name__ == '__main__':
    unittest.main()
