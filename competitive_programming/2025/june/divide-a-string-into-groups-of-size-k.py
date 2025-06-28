"""
Created Date: 2025-06-22
Qn: A string s can be partitioned into groups of size k using the following
    procedure:

    The first group consists of the first k characters of the string, the
    second group consists of the next k characters of the string, and so on.
    Each element can be a part of exactly one group. For the last group, if the
    string does not have k characters remaining, a character fill is used to
    complete the group. Note that the partition is done so that after removing
    the fill character from the last group (if it exists) and concatenating all
    the groups in order, the resultant string should be s.

    Given the string s, the size of each group k and the character fill, return
    a string array denoting the composition of every group s has been divided
    into, using the above procedure.
Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
Notes:
"""

import unittest
from itertools import batched, chain


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        n = len(s)
        filln = k - (n % k) if n % k > 0 else 0
        ns = s + (fill * filln)
        return [ns[b : b + k] for b in range(0, len(ns), k)]

        # Without batched
        # n = len(s)
        # filln = k - (n % k) if n % k > 0 else 0
        # return [''.join(b) for b in batched(chain(s, fill * filln), k)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_divideString1(self):
        s, k, f = "abcdefghi", 3, "x"
        expected = ["abc", "def", "ghi"]
        self.assertEqual(expected, self.sol.divideString(s, k, f))

    def test_divideString2(self):
        s, k, f = "abcdefghij", 3, "x"
        expected = ["abc", "def", "ghi", "jxx"]
        self.assertEqual(expected, self.sol.divideString(s, k, f))


if __name__ == '__main__':
    unittest.main()
