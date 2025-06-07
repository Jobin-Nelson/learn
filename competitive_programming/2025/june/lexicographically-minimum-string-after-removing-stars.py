"""
Created Date: 2025-06-07
Qn: You are given a string s. It may contain any number of '*' characters. Your
    task is to remove all '*' characters.

    While there is a '*', do the following operation:

    - Delete the leftmost '*' and the smallest non-'*' character to its left.
      If there are several smallest characters, you can delete any of them.

    Return the lexicographically smallest resulting string after removing all
    '*' characters.
Link: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
Notes:
    - use stack
"""

import unittest


class Solution:
    def clearStars(self, s: str) -> str:
        freq = [[] for _ in range(26)]
        res = list(s)
        for i, c in enumerate(res):
            if c != '*':
                freq[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if freq[j]:
                        res[freq[j].pop()] = '*'
                        break
        return ''.join(c for c in res if c != '*')


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_clearStars1(self):
        s = "aaba*"
        expected = "aab"
        self.assertEqual(expected, self.sol.clearStars(s))

    def test_clearStars2(self):
        s = "abc"
        expected = "abc"
        self.assertEqual(expected, self.sol.clearStars(s))


if __name__ == '__main__':
    unittest.main()
