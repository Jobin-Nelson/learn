"""
Created Date: 2025-08-13
Qn: Given an integer n, return true if it is a power of three. Otherwise,
    return false.

    An integer n is a power of three, if there exists an integer x such that n
    == 3^x.
Link: https://leetcode.com/problems/power-of-three/
Notes:
    - keep dividing till you get 1
"""

import unittest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n != 0 and n % 3 == 0:
            n //= 3
        return n == 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isPowerOfThree1(self):
        n = 27
        expected = True
        self.assertEqual(expected, self.sol.isPowerOfThree(n))

    def test_isPowerOfThree2(self):
        n = 0
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfThree(n))

    def test_isPowerOfThree3(self):
        n = -1
        expected = False
        self.assertEqual(expected, self.sol.isPowerOfThree(n))


if __name__ == '__main__':
    unittest.main()
