"""
Created Date: 2025-01-09
Qn: You are given an array of strings words and a string pref.

    Return the number of strings in words that contain pref as a prefix.

    A prefix of a string s is any leading contiguous substring of s.
Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/
Notes:
"""

import unittest


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_prefixCount1(self):
        w = ["pay", "attention", "practice", "attend"]
        p = "at"
        expected = 2
        self.assertEqual(expected, self.sol.prefixCount(w, p))

    def test_prefixCount2(self):
        w = ["leetcode", "win", "loops", "success"]
        p = "code"
        expected = 0
        self.assertEqual(expected, self.sol.prefixCount(w, p))


if __name__ == '__main__':
    unittest.main()
