"""
Created Date: 2025-05-25
Qn: You are given an array of strings words. Each element of words consists of
    two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from
    words and concatenating them in any order. Each element can be selected at
    most once.

    Return the length of the longest palindrome that you can create. If it is
    impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.
Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        f = Counter(words)

        total = 0
        extra = 0
        for k, v in f.items():
            if k[0] == k[1]:
                if v & 1 == 1:
                    extra = 1
                total += (v // 2) * 4
            else:
                rk = k[1] + k[0]
                total += min(v, f[rk]) * 2
        return total + extra * 2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestPalindrome1(self):
        w = ["lc", "cl", "gg"]
        expected = 6
        self.assertEqual(expected, self.sol.longestPalindrome(w))

    def test_longestPalindrome2(self):
        w = ["ab", "ty", "yt", "lc", "cl", "ab"]
        expected = 8
        self.assertEqual(expected, self.sol.longestPalindrome(w))

    def test_longestPalindrome3(self):
        w = ["cc", "ll", "xx"]
        expected = 2
        self.assertEqual(expected, self.sol.longestPalindrome(w))


if __name__ == '__main__':
    unittest.main()
