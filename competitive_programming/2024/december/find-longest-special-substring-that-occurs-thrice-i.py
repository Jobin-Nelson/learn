"""
Created Date: 2024-12-10
Qn: You are given a string s that consists of lowercase English letters.

    A string is called special if it is made up of only a single character. For
    example, the string "abc" is not special, whereas the strings "ddd", "zz",
    and "f" are special.

    Return the length of the longest special substring of s which occurs at
    least thrice, or -1 if no special substring occurs at least thrice.

    A substring is a contiguous non-empty sequence of characters within a
    string.
Link: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
Notes:
    - use counter to count the characters and substring cumulatively
"""

import unittest
from itertools import takewhile, groupby


class Solution:
    def maximumLength(self, s: str) -> int:
        # Functional approach
        count = groupby(
            sorted(
                (c2, substr_len)
                for start, c2 in enumerate(s)
                for substr_len, _ in enumerate(
                    takewhile(lambda c: c == c2, s[start:]), start=1
                )
            )
        )
        res = max(
            (v for (_, v), g in count if sum(1 for _ in g) >= 3),
            default=0,
        )
        return res if res != 0 else -1

        # Imperative approach
        # count = {}
        # for start, c1 in enumerate(s):
        #     substring_length = 0
        #     for c2 in s[start:]:
        #         if c2 == c1:
        #             substring_length += 1
        #             count[(c2, substring_length)] = (
        #                 count.get((c2, substring_length), 0) + 1
        #             )
        #         else:
        #             break
        # res = 0
        # for (_, substring_length), freq in count.items():
        #     if freq >= 3 and substring_length > res:
        #         res = substring_length
        # return res if res != 0 else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumLength1(self):
        s = "a" * 4
        expected = 2
        self.assertEqual(expected, self.sol.maximumLength(s))

    def test_maximumLength2(self):
        s = "abcdef"
        expected = -1
        self.assertEqual(expected, self.sol.maximumLength(s))

    def test_maximumLength3(self):
        s = "abcaba"
        expected = 1
        self.assertEqual(expected, self.sol.maximumLength(s))


if __name__ == '__main__':
    unittest.main()
