"""
Created Date: 2025-01-08
Qn: You are given a 0-indexed string array words.

    Let's define a boolean function isPrefixAndSuffix that takes two strings,
    str1 and str2:

    isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a
    suffix of str2, and false otherwise. For example, isPrefixAndSuffix("aba",
    "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
    but isPrefixAndSuffix("abc", "abcd") is false.

    Return an integer denoting the number of index pairs (i, j) such that i <
    j, and isPrefixAndSuffix(words[i], words[j]) is true.
Link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
Notes:
    - use dual trie
"""

import unittest
from collections import defaultdict


class Solution:
    def countPairsSuffixPairs(self, words: list[str]) -> int:
        root = (T := lambda: defaultdict(T))()
        res = 0
        for w in words:
            x = root
            for k in zip(w, reversed(w)):
                res += (x := x[k]).get(0, 0)
            x[0] = x.get(0, 0) + 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countPairsSuffixPairs1(self):
        w = ["a", "aba", "ababa", "aa"]
        expected = 4
        self.assertEqual(expected, self.sol.countPairsSuffixPairs(w))

    def test_countPairsSuffixPairs2(self):
        w = ["pa","papa","ma","mama"]
        expected = 2
        self.assertEqual(expected, self.sol.countPairsSuffixPairs(w))

    def test_countPairsSuffixPairs3(self):
        w = ["abab", "ab"]
        expected = 0
        self.assertEqual(expected, self.sol.countPairsSuffixPairs(w))


if __name__ == '__main__':
    unittest.main()
