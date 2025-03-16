"""
Created Date: 2025-03-14
Qn: You are given a 0-indexed integer array candies. Each element in the array
    denotes a pile of candies of size candies[i]. You can divide each pile into
    any number of sub piles, but you cannot merge two piles together.

    You are also given an integer k. You should allocate piles of candies to k
    children such that each child gets the same number of candies. Each child
    can be allocated candies from only one pile of candies and some piles of
    candies may go unused.

    Return the maximum number of candies each child can get.
Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
Notes:
    - use binary search
"""

import unittest
from itertools import accumulate


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        total_candies = sum(candies)
        if total_candies < k:
            return 0

        def satisfy(num: int) -> bool:
            return any(
                cum >= k
                for cum in accumulate(c // num for c in candies if c >= num)
            )

        l, r = 1, total_candies // k
        while l <= r:
            m = l + ((r - l) >> 1)
            if satisfy(m):
                l = m + 1
            else:
                r = m - 1
        return r


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumCandies1(self):
        c = [5, 8, 6]
        k = 3
        expected = 5
        self.assertEqual(expected, self.sol.maximumCandies(c, k))

    def test_maximumCandies2(self):
        c = [2, 5]
        k = 11
        expected = 0
        self.assertEqual(expected, self.sol.maximumCandies(c, k))

    def test_maximumCandies3(self):
        c = [4, 7, 5]
        k = 4
        expected = 3
        self.assertEqual(expected, self.sol.maximumCandies(c, k))


if __name__ == '__main__':
    unittest.main()
