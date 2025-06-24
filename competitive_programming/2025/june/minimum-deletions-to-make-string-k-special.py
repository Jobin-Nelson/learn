"""
Created Date: 2025-06-21
Qn: You are given a string word and an integer k.

    We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k
    for all indices i and j in the string.

    Here, freq(x) denotes the frequency of the character x in word, and |y|
    denotes the absolute value of y.

    Return the minimum number of characters you need to delete to make word
    k-special.
Link: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
Notes:
    - iterate through each element and clip between the value and value + k
"""

import unittest
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        return min((
            sum(b if a > b else b - (a + k) if b > a + k else 0 for b in freq.values())
            for a in freq.values()),
            default=len(word),
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumDeletions1(self):
        w, k = "aabcaba", 0
        expected = 3
        self.assertEqual(expected, self.sol.minimumDeletions(w, k))

    def test_minimumDeletions2(self):
        w, k = "dabdcbdcdcd", 2
        expected = 2
        self.assertEqual(expected, self.sol.minimumDeletions(w, k))

    def test_minimumDeletions3(self):
        w, k = "aaabaaa", 2
        expected = 1
        self.assertEqual(expected, self.sol.minimumDeletions(w, k))


if __name__ == '__main__':
    unittest.main()
