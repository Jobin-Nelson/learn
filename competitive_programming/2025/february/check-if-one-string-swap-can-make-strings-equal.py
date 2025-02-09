"""
Created Date: 2025-02-05
Qn: You are given two strings s1 and s2 of equal length. A string swap is an
    operation where you choose two indices in a string (not necessarily
    different) and swap the characters at these indices.

    Return true if it is possible to make both strings equal by performing at
    most one string swap on exactly one of the strings. Otherwise, return
    false.
Link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
Notes:
"""

import unittest


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        return not res or (
            len(res) == 2 and s1[res[0]] == s2[res[1]] and s1[res[1]] == s2[res[0]]
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_areAlmostEqual1(self):
        s1, s2 = "bank", "kanb"
        expected = True
        self.assertEqual(expected, self.sol.areAlmostEqual(s1, s2))

    def test_areAlmostEqual2(self):
        s1, s2 = "attack", "defend"
        expected = False
        self.assertEqual(expected, self.sol.areAlmostEqual(s1, s2))

    def test_areAlmostEqual3(self):
        s1, s2 = "kelb", "kelb"
        expected = True
        self.assertEqual(expected, self.sol.areAlmostEqual(s1, s2))


if __name__ == '__main__':
    unittest.main()
