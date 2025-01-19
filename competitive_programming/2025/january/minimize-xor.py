"""
Created Date: 2025-01-15
Qn: Given two positive integers num1 and num2, find the positive integer x such
    that:

    - x has the same number of set bits as num2, and
    - The value x XOR num1 is minimal.

    Note that XOR is the bitwise XOR operation.

    Return the integer x. The test cases are generated such that x is uniquely
    determined.

    The number of set bits of an integer is the number of 1's in its binary
    representation.
Link: https://leetcode.com/problems/minimize-xor/
Notes:
"""

import unittest


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = num2.bit_count()

        res = 0
        for i in range(32, -1, -1):
            if (num1 & (1 << i)) > 0 and count > 0:
                res |= 1 << i
                count -= 1

        for i in range(32):
            if count > 0 and (res & (1 << i)) == 0:
                res |= 1 << i
                count -= 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimizeXor1(self):
        n1, n2 = 3, 5
        expected = 3
        self.assertEqual(expected, self.sol.minimizeXor(n1, n2))

    def test_minimizeXor2(self):
        n1, n2 = 1, 12
        expected = 3
        self.assertEqual(expected, self.sol.minimizeXor(n1, n2))


if __name__ == '__main__':
    unittest.main()
