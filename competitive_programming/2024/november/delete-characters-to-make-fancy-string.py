"""
Created Date: 2024-11-01
Qn: A fancy string is a string where no three consecutive characters are equal.

    Given a string s, delete the minimum possible number of characters from s
    to make it fancy.

    Return the final string after the deletion. It can be shown that the answer
    will always be unique.
Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
Notes:
    - use count
"""

import unittest


class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = ''
        count = 1
        res = []
        for c in s:
            if c == prev:
                if count == 2:
                    continue
                count += 1
            else:
                count = 1
                prev = c
            res.append(c)
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_makeFancyString1(self):
        s = "leeetcode"
        self.assertEqual(self.sol.makeFancyString(s), "leetcode")
    def test_makeFancyString2(self):
        s = "aaabaaaa"
        self.assertEqual(self.sol.makeFancyString(s), "aabaa")
    def test_makeFancyString3(self):
        s = "aab"
        self.assertEqual(self.sol.makeFancyString(s), "aab")


if __name__ == '__main__':
    unittest.main()
