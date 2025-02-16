"""
Created Date: 2025-02-10
Qn: You are given a string s.

    Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.
    Return the resulting string after removing all digits.
Link: https://leetcode.com/problems/clear-digits/
Notes:
    - use stack
"""

import unittest


class Solution:
    def clearDigits(self, s: str) -> str:
        alphas = []
        for c in s:
            if c.isdecimal():
                if alphas:
                    alphas.pop()
            else:
                alphas.append(c)
        return ''.join(alphas)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_clearDigits1(self):
        s = "abc"
        expected = "abc"
        self.assertEqual(expected, self.sol.clearDigits(s))

    def test_clearDigits2(self):
        s = "cb34"
        expected = ""
        self.assertEqual(expected, self.sol.clearDigits(s))


if __name__ == '__main__':
    unittest.main()
