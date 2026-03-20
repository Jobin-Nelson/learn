"""
Created Date: 2026-03-11
Qn: The complement of an integer is the integer you get when you flip all the
    0's to 1's and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010"
    which is the integer 2. Given an integer n, return its complement.
Link: https://leetcode.com/problems/complement-of-base-10-integer/
Notes:
"""

import unittest


class Solution:
    def bitwiseComplete(self, n: int) -> int:
        if n == 0:
            return 1
        bit_length = n.bit_length()
        full_mask = 0
        for _ in range(bit_length):
            full_mask <<= 1
            full_mask |= 1
        return full_mask ^ n


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 5
        expected = 2
        self.assertEqual(expected, self.sol.bitwiseComplete(n))

    def test2(self):
        n = 7
        expected = 0
        self.assertEqual(expected, self.sol.bitwiseComplete(n))


if __name__ == '__main__':
    unittest.main()
