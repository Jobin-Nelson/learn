"""
Created Date: 2025-03-30
Qn:You are given a string s. We want to partition the string into as many parts
    as possible so that each letter appears in at most one part. For example,
    the string "ababcc" can be partitioned into ["abab", "cc"], but partitions
    such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

    Note that the partition is done so that after concatenating all the parts
    in order, the resultant string should be s.

    Return a list of integers representing the size of these parts.
Link: https://leetcode.com/problems/partition-labels/
Notes:
    - keep track of start and end occurance of each character
"""

import unittest


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        N = len(s) - 1
        lookup = [(N, N)] * 26
        ord_a = ord('a')

        for i, c in enumerate(s):
            ind = ord(c) - ord_a
            if lookup[ind] == (N, N):
                lookup[ind] = (i, i)
            else:
                lookup[ind] = (lookup[ind][0], i)

        res = []
        count = 0
        prev_part_ind = 0
        for i, c in enumerate(s):
            ind = ord(c) - ord_a
            start, end = lookup[ind]
            if i == start:
                count += 1
            if i == end:
                count -= 1
            if count == 0:
                res.append(i - prev_part_ind + 1)
                prev_part_ind = i + 1

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_partitionLabels1(self):
        s = "ababcbacadefegdehijhklij"
        expected = [9, 7, 8]
        self.assertEqual(expected, self.sol.partitionLabels(s))

    def test_partitionLabels2(self):
        s = "eccbbbbdec"
        expected = [10]
        self.assertEqual(expected, self.sol.partitionLabels(s))


if __name__ == '__main__':
    unittest.main()
