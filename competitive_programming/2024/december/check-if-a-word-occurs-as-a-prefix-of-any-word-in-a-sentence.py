"""
Created Date: 2024-12-02
Qn: Given a sentence that consists of some words separated by a single space,
    and a searchWord, check if searchWord is a prefix of any word in sentence.

    Return the index of the word in sentence (1-indexed) where searchWord is a
    prefix of this word. If searchWord is a prefix of more than one word,
    return the index of the first word (minimum index). If there is no such
    word return -1.

    A prefix of a string s is any leading contiguous substring of s.
Link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
Notes:
"""

import unittest


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next((i+1 for (i, w) in enumerate(sentence.split()) if w.startswith(searchWord)), -1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isPrefixOfWord1(self):
        se = "i love eating burger"
        sw = "burg"
        self.assertEqual(4, self.sol.isPrefixOfWord(se, sw))
    def test_isPrefixOfWord2(self):
        se = "this problem is an easy problem"
        sw = "pro"
        self.assertEqual(2, self.sol.isPrefixOfWord(se, sw))
    def test_isPrefixOfWord3(self):
        se = "i am tired"
        sw = "you"
        self.assertEqual(-1, self.sol.isPrefixOfWord(se, sw))


if __name__ == '__main__':
    unittest.main()
