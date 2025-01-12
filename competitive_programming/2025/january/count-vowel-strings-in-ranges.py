"""
Created Date: 2025-01-02
Qn: You are given a 0-indexed array of strings words and a 2D array of integers
    queries.

    Each query queries[i] = [li, ri] asks us to find the number of strings
    present in the range li to ri (both inclusive) of words that start and end
    with a vowel.

    Return an array ans of size queries.length, where ans[i] is the answer to
    the ith query.
Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/
Notes:
    - use prefix to quickly calculate the score within a range
"""

import unittest
from itertools import accumulate


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        # Functional approach
        vowels = list('aeiou')

        prefix_count = list(
            accumulate([w[0] in vowels and w[-1] in vowels for w in words], initial=0)
        )

        def to_count(range: list[int]) -> int:
            return prefix_count[range[1] + 1] - prefix_count[range[0]]

        return [to_count(q) for q in queries]

        # Imperative approach
        # vowels = list('aeiou')
        # prefix_count = [0] * (len(words) + 1)
        # for i, s in enumerate(words):
        #     prefix_count[i + 1] = (
        #         prefix_count[i] + 1
        #         if s[0] in vowels and s[-1] in vowels
        #         else prefix_count[i]
        #     )
        #
        # def to_count(range: list[int]) -> int:
        #     return (
        #         prefix_count[range[1]+1] - prefix_count[range[0]]
        #     )
        #
        # return [to_count(q) for q in queries]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_vowelStrings1(self):
        w = ["aba", "bcb", "ece", "aa", "e"]
        q = [[0, 2], [1, 4], [1, 1]]
        expected = [2, 3, 0]
        self.assertEqual(expected, self.sol.vowelStrings(w, q))

    def test_vowelStrings2(self):
        w = ["a", "e", "i"]
        q = [[0, 2], [0, 1], [2, 2]]
        expected = [3, 2, 1]
        self.assertEqual(expected, self.sol.vowelStrings(w, q))


if __name__ == '__main__':
    unittest.main()
