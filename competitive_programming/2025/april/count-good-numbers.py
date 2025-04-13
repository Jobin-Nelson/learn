"""
Created Date: 2025-04-13
Qn: A digit string is good if the digits (0-indexed) at even indices are even
    and the digits at odd indices are prime (2, 3, 5, or 7).

    - For example, "2582" is good because the digits (2 and 8) at even
      positions are even and the digits (5 and 2) at odd positions are prime.
      However, "3245" is not good because 3 is at an even index but is not
      even.

    Given an integer n, return the total number of good digit strings of length
    n. Since the answer may be large, return it modulo 109 + 7.

    A digit string is a string consisting of digits 0 through 9 that may
    contain leading zeros.
Link: https://leetcode.com/problems/count-good-numbers/
Notes:
"""

import unittest


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        odd = n >> 1
        even = n - odd
        return (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countGoodNumbers1(self):
        n = 1
        expected = 5
        self.assertEqual(expected, self.sol.countGoodNumbers(n))

    def test_countGoodNumbers2(self):
        n = 4
        expected = 400
        self.assertEqual(expected, self.sol.countGoodNumbers(n))

    def test_countGoodNumbers3(self):
        n = 50
        expected = 564908303
        self.assertEqual(expected, self.sol.countGoodNumbers(n))


if __name__ == '__main__':
    unittest.main()
