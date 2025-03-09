"""
Created Date: 2025-03-04
Qn: Given an integer n, return true if it is possible to represent n as the sum
    of distinct powers of three. Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y
    == 3x.
Link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
Notes:
    - take the largest power of 3 less than number
    - keep subtracting the powers of 3 till the number is 0
"""

import unittest


class Solution:
    def checkPowerOfThree(self, n: int) -> bool:
        i = 0
        while 3 ** (i + 1) <= n:
            i += 1

        while i >= 0:
            power = 3**i
            if power <= n:
                n -= power
            i -= 1
        return n == 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_checkPowerOfThree1(self):
        n = 12
        expected = True
        self.assertEqual(expected, self.sol.checkPowerOfThree(n))

    def test_checkPowerOfThree2(self):
        n = 91
        expected = True
        self.assertEqual(expected, self.sol.checkPowerOfThree(n))

    def test_checkPowerOfThree3(self):
        n = 21
        expected = False
        self.assertEqual(expected, self.sol.checkPowerOfThree(n))


if __name__ == '__main__':
    unittest.main()
