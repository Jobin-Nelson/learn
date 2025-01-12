"""
Created Date: 2025-01-07
Qn: Given an array of string words, return all strings in words that is a
    substring of another word. You can return the answer in any order.

    A substring is a contiguous sequence of characters within a string
Link: https://leetcode.com/problems/string-matching-in-an-array/
Notes:
"""

import unittest


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        # Functional approach
        return list({
            w1
            for i, w1 in enumerate(words)
            for j, w2 in enumerate(words)
            if i != j and w1 in w2
        })

        # Imperative appraoch
        # N = len(words)
        # res = []
        # for i in range(N):
        #     for j in range(N):
        #         if i == j: continue
        #         if words[i] in words[j]:
        #             res.append(words[i])
        #             break
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_stringMatching1(self):
        w = ["mass", "as", "hero", "superhero"]
        expected = ["as", "hero"]
        self.assertEqual(expected, self.sol.stringMatching(w))

    def test_stringMatching2(self):
        w = ["mass", "as", "hero", "superhero"]
        expected = ["as", "hero"]
        self.assertEqual(expected, self.sol.stringMatching(w))


if __name__ == '__main__':
    unittest.main()
