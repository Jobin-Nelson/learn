"""
Created Date: 2025-05-24
Qn: You are given a 0-indexed array of strings words and a character x.

    Return an array of indices representing the words that contain the
    character x.

    Note that the returned array may be in any order.
Link: https://leetcode.com/problems/find-words-containing-character/
Notes:
"""

import unittest


class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, w in enumerate(words) if x in w]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findWordsContaining1(self):
        w = ["leet", "code"]
        x = 'e'
        expected = [0, 1]
        self.assertEqual(expected, self.sol.findWordsContaining(w, x))

    def test_findWordsContaining2(self):
        w = ["abc", "bcd", "aaaa", "cbc"]
        x = 'a'
        expected = [0, 2]
        self.assertEqual(expected, self.sol.findWordsContaining(w, x))

    def test_findWordsContaining3(self):
        w = ["abc", "bcd", "aaaa", "cbc"]
        x = 'z'
        expected = []
        self.assertEqual(expected, self.sol.findWordsContaining(w, x))


if __name__ == '__main__':
    unittest.main()
