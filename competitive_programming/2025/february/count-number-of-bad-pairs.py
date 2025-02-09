"""
Created Date: 2025-02-09
Qn: You are given a 0-indexed integer array nums. A pair of indices (i, j) is a
    bad pair if i < j and j - i != nums[j] - nums[i].

    Return the total number of bad pairs in nums.
Link: https://leetcode.com/problems/count-number-of-bad-pairs/
Notes:
    - use total - good pairs
"""

import unittest
from itertools import combinations
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        # Functional approach (TLE)
        # return sum(
        #     1 for a, b in combinations(enumerate(nums), 2) if b[1] - a[1] != b[0] - a[0]
        # )
        # Imerative approach
        good_pairs = 0
        total_pairs = 0
        count = defaultdict(int)

        for i, n in enumerate(nums):
            total_pairs += i
            good_pairs += count[n - i]
            count[n - i] += 1
        return total_pairs - good_pairs


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countBadPairs1(self):
        n = [4, 1, 3, 3]
        expected = 5
        self.assertEqual(expected, self.sol.countBadPairs(n))

    def test_countBadPairs2(self):
        n = list(range(1, 6))
        expected = 0
        self.assertEqual(expected, self.sol.countBadPairs(n))


if __name__ == '__main__':
    unittest.main()
