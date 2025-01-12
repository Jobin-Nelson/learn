"""
Created Date: 2025-01-01
Qn: Given a string s of zeros and ones, return the maximum score after
    splitting the string into two non-empty substrings (i.e. left substring and
    right substring).

    The score after splitting a string is the number of zeros in the left
    substring plus the number of ones in the right substring.
Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
Notes:
"""

from operator import sub
import unittest
from itertools import accumulate, starmap
from typing import TypeAlias


ZeroOne: TypeAlias = tuple[int, int]


class Solution:
    def maxScore(self, s: str) -> int:
        # Functional approach
        # score = Zl + Or
        # score = Zl + Ot - Ol
        # score = Ot(constant) + Zl - Ol
        def to_zero_one(c: str) -> ZeroOne:
            return (1, 0) if c == '0' else (0, 1)

        def add_zero_one(x: ZeroOne, y: ZeroOne) -> ZeroOne:
            return x[0] + y[0], x[1] + y[1]
            # return tuple(starmap(add, zip(x, y)))

        score = max(starmap(sub, accumulate(map(to_zero_one, s[:-1]), add_zero_one)))
        return score + s.count('1')

        # Imperative approach
        # res = -maxsize
        # cur_zero_count = 0
        # cur_one_count = 0
        # for c in s[:-1]:
        #     if c == '0':
        #         cur_zero_count += 1
        #     else:
        #         cur_one_count += 1
        #     res = max(res, cur_zero_count - cur_one_count)
        #
        # if s[-1] == '1':
        #     cur_one_count += 1
        # return res + cur_one_count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxScore1(self):
        s = '011101'
        expected = 5
        self.assertEqual(expected, self.sol.maxScore(s))

    def test_maxScore2(self):
        s = '00111'
        expected = 5
        self.assertEqual(expected, self.sol.maxScore(s))

    def test_maxScore3(self):
        s = '1111'
        expected = 3
        self.assertEqual(expected, self.sol.maxScore(s))


if __name__ == '__main__':
    unittest.main()
    # Solution().maxScore('00111')
