"""
Created Date: 2025-06-27
Qn: You are given a string s of length n, and an integer k. You are tasked to
    find the longest subsequence repeated k times in string s.

    A subsequence is a string that can be derived from another string by
    deleting some or no characters without changing the order of the remaining
    characters.

    A subsequence seq is repeated k times in the string s if seq * k is a
    subsequence of s, where seq * k represents a string constructed by
    concatenating seq k times.

    - For example, "bba" is repeated 2 times in the string "bababcba", because
      the string "bbabba", constructed by concatenating "bba" 2 times, is a
      subsequence of the string "bababcba".

    Return the longest subsequence repeated k times in string s. If multiple
    such subsequences are found, return the lexicographically largest one. If
    there is no such subsequence, return an empty string.
Link: https://leetcode.com/problems/longest-subsequence-repeated-k-times/
Notes:
"""

import unittest
from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ''
        candidates = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)
        q = deque(candidates)
        while q:
            cur = q.popleft()
            if len(cur) > len(res):
                res = cur
            for ch in candidates:
                nxt = cur + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestSubsequenceRepeatedK1(self):
        s = "letsleetcode"
        k = 2
        expected = "let"
        self.assertEqual(expected, self.sol.longestSubsequenceRepeatedK(s, k))

    def test_longestSubsequenceRepeatedK2(self):
        s = "bb"
        k = 2
        expected = "b"
        self.assertEqual(expected, self.sol.longestSubsequenceRepeatedK(s, k))

    def test_longestSubsequenceRepeatedK3(self):
        s = "ab"
        k = 2
        expected = ""
        self.assertEqual(expected, self.sol.longestSubsequenceRepeatedK(s, k))


if __name__ == '__main__':
    unittest.main()
