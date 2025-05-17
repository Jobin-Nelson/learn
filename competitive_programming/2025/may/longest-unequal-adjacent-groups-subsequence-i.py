"""
Created Date: 2025-05-15
Qn: You are given a string array words and a binary array groups both of length
    n, where words[i] is associated with groups[i].

    Your task is to select the longest alternating subsequence from words. A
    subsequence of words is alternating if for any two consecutive strings in
    the sequence, their corresponding elements in the binary array groups
    differ. Essentially, you are to choose strings such that adjacent elements
    have non-matching corresponding bits in the groups array.

    Formally, you need to find the longest subsequence of an array of indices
    [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] !=
    groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding
    to these indices.

    Return the selected subsequence. If there are multiple answers, return any
    of them.

    Note: The elements in words are distinct.
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
Notes:
"""

import unittest


class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        return [words[0]] + [
            words[i] for i in range(1, len(groups)) if groups[i] != groups[i - 1]
        ]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_getLongestSubsequence1(self):
        w, g = ['e', 'a', 'b'], [0, 0, 1]
        expected = ['e', 'b']
        self.assertEqual(expected, self.sol.getLongestSubsequence(w, g))

    def test_getLongestSubsequence2(self):
        w, g = ["a", "b", "c", "d"], [1, 0, 1, 1]
        expected = ["a", "b", "c"]
        self.assertEqual(expected, self.sol.getLongestSubsequence(w, g))


if __name__ == '__main__':
    unittest.main()
