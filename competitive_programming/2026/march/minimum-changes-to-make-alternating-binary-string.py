"""
Created Date: 2026-03-05
Qn: You are given a string s consisting only of the characters '0' and '1'. In
    one operation, you can change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal.
    For example, the string "010" is alternating, while the string "0100" is
    not.

    Return the minimum number of operations needed to make s alternating.
Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
Notes:
"""

import unittest


class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        for i, d in enumerate(s):
            if i & 1:
                if d == '0':
                    start0 += 1
            else:
                if d == '1':
                    start0 += 1
        return min(start0, len(s) - start0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = "0100"
        expected = 1
        self.assertEqual(expected, self.sol.minOperations(s))

    def test2(self):
        s = "10"
        expected = 0
        self.assertEqual(expected, self.sol.minOperations(s))

    def test3(self):
        s = "1111"
        expected = 2
        self.assertEqual(expected, self.sol.minOperations(s))


if __name__ == '__main__':
    unittest.main()
