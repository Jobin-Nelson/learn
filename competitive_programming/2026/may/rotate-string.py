"""
Created Date: 2026-05-03
Qn: Given two strings s and goal, return true if and only if s can become goal
    after some number of shifts on s.

    A shift on s consists of moving the leftmost character of s to the
    rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.
Link: https://leetcode.com/problems/rotate-string/
Notes:
    - us sliding window
"""

import unittest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n, space = len(s), s + s
        return any(space[i : i + n] == goal for i in range(n))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s, g = "abcde", "cdeab"
        expected = True
        self.assertEqual(expected, self.sol.rotateString(s, g))

    def test2(self):
        s, g = "abcde", "abced"
        expected = False
        self.assertEqual(expected, self.sol.rotateString(s, g))


if __name__ == '__main__':
    unittest.main()
