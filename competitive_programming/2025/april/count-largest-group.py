"""
Created Date: 2025-04-23
Qn: You are given an integer n.

    Each number from 1 to n is grouped according to the sum of its digits.

    Return the number of groups that have the largest size.
Link: https://leetcode.com/problems/count-largest-group/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = Counter()
        for i in range(1, n + 1):
            key = sum(int(x) for x in str(i))
            hashmap[key] += 1
        maxValue = max(hashmap.values())
        return sum(1 for c in hashmap.values() if c == maxValue)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countLargestGroup1(self):
        n = 13
        expected = 4
        self.assertEqual(expected, self.sol.countLargestGroup(n))

    def test_countLargestGroup2(self):
        n = 13
        expected = 4
        self.assertEqual(expected, self.sol.countLargestGroup(n))


if __name__ == '__main__':
    unittest.main()
