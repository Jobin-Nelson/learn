"""
Created Date: 2024-11-04
Qn: Given a string word, compress it using the following algorithm:

    Begin with an empty string comp. While word is not empty, use the following
    operation: Remove a maximum length prefix of word made of a single
    character c repeating at most 9 times. Append the length of the prefix
    followed by c to comp. Return the string comp.
Link: https://leetcode.com/problems/string-compression-iii/
Notes:
"""

import unittest
from itertools import groupby


class Solution:
    def compressedString(self, word: str) -> str:
        # functional approach
        res = []
        for key, group in groupby(word):
            count = len(list(group))
            while count > 9:
                res.append(f'9{key}')
                count -= 9
            res.append(f'{count}{key}')
        return ''.join(res)

        # res = []
        # prev = word[0]
        # count = 1
        # for c in word[1:]:
        #     if c != prev or count == 9:
        #         res.append(f'{count}{prev}')
        #         count = 0
        #     prev = c
        #     count += 1
        # res.append(f'{count}{prev}')
        # return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_compressedString1(self):
        w = "abcde"
        self.assertEqual(self.sol.compressedString(w), "1a1b1c1d1e")

    def test_compressedString2(self):
        w = "aaaaaaaaaaaaaabb"
        self.assertEqual(self.sol.compressedString(w), "9a5a2b")


if __name__ == '__main__':
    unittest.main()
