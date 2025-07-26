"""
Created Date: 2025-07-21
Qn: A fancy string is a string where no three consecutive characters are equal.

    Given a string s, delete the minimum possible number of characters from s to
    make it fancy.

    Return the final string after the deletion. It can be shown that the answer
    will always be unique.
Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
Notes:
"""

import unittest


class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        res = []
        prev = ''
        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1

            if count < 3:
                res.append(c)
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_makeFancyString1(self):
        s = "leeetcode"
        expected = "leetcode"
        self.assertEqual(expected, self.sol.makeFancyString(s))

    def test_makeFancyString2(self):
        s = "aaabaaaa"
        expected = "aabaa"
        self.assertEqual(expected, self.sol.makeFancyString(s))

    def test_makeFancyString3(self):
        s = "aab"
        expected = "aab"
        self.assertEqual(expected, self.sol.makeFancyString(s))


if __name__ == '__main__':
    unittest.main()
