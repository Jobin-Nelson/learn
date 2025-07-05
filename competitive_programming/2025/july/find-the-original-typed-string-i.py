"""
Created Date: 2025-07-01
Qn: Alice is attempting to type a specific string on her computer. However, she
    tends to be clumsy and may press a key for too long, resulting in a
    character being typed multiple times.

    Although Alice tried to focus on her typing, she is aware that she may
    still have done this at most once.

    You are given a string word, which represents the final output displayed on
    Alice's screen.

    Return the total number of possible original strings that Alice might have
    intended to type.
Link: https://leetcode.com/problems/find-the-original-typed-string-i/
Notes:
    - count equal adjacent elements - 1
"""

import unittest
from itertools import pairwise


class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Functional approach
        return 1 + sum(1 for c1, c2 in pairwise(word) if c1 == c2)

        # Imperative approach
        # res, n = 1, len(word)
        # for i in range(1, n):
        #     if word[i-1] == word[i]:
        #         res += 1
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_possibleStringCount1(self):
        w = "abbcccc"
        expected = 5
        self.assertEqual(expected, self.sol.possibleStringCount(w))

    def test_possibleStringCount2(self):
        w = "abcd"
        expected = 1
        self.assertEqual(expected, self.sol.possibleStringCount(w))

    def test_possibleStringCount3(self):
        w = "aaaa"
        expected = 4
        self.assertEqual(expected, self.sol.possibleStringCount(w))


if __name__ == '__main__':
    unittest.main()
