"""
Created Date: 2025-01-04
Qn: Given a string s, return the number of unique palindromes of length three
    that are a subsequence of s.

    Note that even if there are multiple ways to obtain the same subsequence,
    it is still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original
    string with some characters (can be none) deleted without changing the
    relative order of the remaining characters.

    - For example, "ace" is a subsequence of "abcde".
Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
Notes:
    - use hashset and use middle character to determine 3 len palindrome
"""

import unittest
from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left, right = set(), Counter(s)
        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((m, c))
            left.add(m)
        return len(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countPalindromicSubsequence1(self):
        s = "aabca"
        expected = 3
        self.assertEqual(expected, self.sol.countPalindromicSubsequence(s))

    def test_countPalindromicSubsequence2(self):
        s = "adc"
        expected = 0
        self.assertEqual(expected, self.sol.countPalindromicSubsequence(s))


if __name__ == '__main__':
    unittest.main()
