"""
Created Date: 2024-12-03
Qn: You are given a 0-indexed string s and a 0-indexed integer array spaces
    that describes the indices in the original string where spaces will be
    added. Each space should be inserted before the character at the given
    index.

    - For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces
      before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we
      obtain "Enjoy Your Coffee".

    Return the modified string after the spaces have been added.
Link: https://leetcode.com/problems/adding-spaces-to-a-string/
Notes:
    - append spaces before each spaces value
"""

import unittest
from itertools import chain, pairwise


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        # Functional approach
        return ' '.join(s[i:j] for i, j in pairwise(chain([0], spaces, [len(s)])))

        # Imperative approch
        # spaced = []
        # prev = 0
        # for start in spaces:
        #     spaced.append(s[prev:start])
        #     prev = start
        # spaced.append(s[prev:])
        # return ' '.join(spaced)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_addSpaces1(self):
        s = "LeetcodeHelpsMeLearn"
        sp = [8, 13, 15]
        expected = "Leetcode Helps Me Learn"
        self.assertEqual(expected, self.sol.addSpaces(s, sp))

    def test_addSpaces2(self):
        s = "icodeinpython"
        sp = [1, 5, 7, 9]
        expected = "i code in py thon"
        self.assertEqual(expected, self.sol.addSpaces(s, sp))

    def test_addSpaces3(self):
        s = "spacing"
        sp = list(range(7))
        expected = " " + " ".join("spacing")
        self.assertEqual(expected, self.sol.addSpaces(s, sp))


if __name__ == '__main__':
    unittest.main()
