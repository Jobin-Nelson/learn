"""
Created Date: 2025-10-29
Qn: You are given a positive number n.

    Return the smallest number x greater than or equal to n, such that the
    binary representation of x contains only set bits
Link: https://leetcode.com/problems/smallest-number-with-all-set-bits/
Notes:
    - use bit length
"""

import unittest


class Solution:
    def smallestNumber(self, n: int) -> int:
        bit_length = n.bit_length()
        res = 0
        for i in range(bit_length):
            res |= (1 << i)
        return res if  n.bit_length() >= n.bit_count() else res | (1 << bit_length)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 5
        expected = 7
        self.assertEqual(expected, self.sol.smallestNumber(n))

    def test2(self):
        n = 10
        expected = 15
        self.assertEqual(expected, self.sol.smallestNumber(n))

    def test3(self):
        n = 3
        expected = 3
        self.assertEqual(expected, self.sol.smallestNumber(n))


if __name__ == '__main__':
    unittest.main()
