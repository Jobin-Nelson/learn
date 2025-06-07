"""
Created Date: 2025-06-04
Qn: You are given a string word, and an integer numFriends.

    Alice is organizing a game for her numFriends friends. There are multiple
    rounds in the game, where in each round:

    - word is split into numFriends non-empty strings, such that no previous
      round has had the exact same split.
    - All the split words are put into a box.

    Find the lexicographically largest string from the box after all the rounds
    are finished.
Link: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
Notes:
"""

import unittest
from functools import reduce


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Functional
        n = len(word)
        length = n - numFriends + 1
        return (
            reduce(lambda acc, x: max(word[x : x + length], acc), range(n), '')
            if numFriends > 1
            else word
        )

        # Imperative
        # if numFriends == 1:
        #     return word
        # n = len(word)
        # best_length = n - numFriends + 1
        #
        # best = ""
        # for i in range(n):
        #     if word[i:i+best_length] > best:
        #         best = word[i:i+best_length]
        # return best


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_answerString1(self):
        w, n = "dbca", 2
        expected = "dbc"
        self.assertEqual(expected, self.sol.answerString(w, n))

    def test_answerString2(self):
        w, n = "gggg", 4
        expected = "g"
        self.assertEqual(expected, self.sol.answerString(w, n))

    def test_answerString3(self):
        w, n = "gh", 1
        expected = "gh"
        self.assertEqual(expected, self.sol.answerString(w, n))

    def test_answerString4(self):
        w, n = "nbjnc", 2
        expected = "nc"
        self.assertEqual(expected, self.sol.answerString(w, n))


if __name__ == '__main__':
    unittest.main()
