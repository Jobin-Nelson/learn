"""
Created Date: 2024-11-03
Qn: Given two strings s and goal, return true if and only if s can become goal
    after some number of shifts on s.

    A shift on s consists of moving the leftmost character of s to the
    rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.
Link: https://leetcode.com/problems/rotate-string/
Notes:
"""

import unittest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        concatinated_string = s + s
        return goal in concatinated_string


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_rotateString1(self):
        s, g = "abcde", "cdeab"
        self.assertEqual(self.sol.rotateString(s,g), True)

    def test_rotateString2(self):
        s, g = "abcde", "abced"
        self.assertEqual(self.sol.rotateString(s,g), False)


if __name__ == '__main__':
    unittest.main()
