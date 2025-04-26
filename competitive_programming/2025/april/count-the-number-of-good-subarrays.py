"""
Created Date: 2025-04-16
Qn: Given an integer array nums and an integer k, return the number of good
    subarrays of nums.

    A subarray arr is good if there are at least k pairs of indices (i, j) such
    that i < j and arr[i] == arr[j].

    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/count-the-number-of-good-subarrays/
Notes:
    - use sliding window
"""

import unittest
from collections import Counter


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        freq = Counter()
        res = 0
        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += freq[nums[right]]
                freq[nums[right]] += 1
            if same >= k:
                res += n - right
            freq[nums[left]] -= 1
            same -= freq[nums[left]]
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countGood1(self):
        n, k = [1, 1, 1, 1, 1], 10
        expected = 1
        self.assertEqual(expected, self.sol.countGood(n, k))

    def test_countGood2(self):
        n, k = [3, 1, 4, 3, 2, 2, 4], 2
        expected = 4
        self.assertEqual(expected, self.sol.countGood(n, k))


if __name__ == '__main__':
    unittest.main()
