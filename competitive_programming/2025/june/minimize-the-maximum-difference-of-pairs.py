"""
Created Date: 2025-06-13
Qn: You are given a 0-indexed integer array nums and an integer p. Find p pairs
    of indices of nums such that the maximum difference amongst all the pairs
    is minimized. Also, ensure no index appears more than once amongst the p
    pairs.

    Note that for a pair of elements at the index i and j, the difference of
    this pair is |nums[i] - nums[j]|, where |x| represents the absolute value
    of x.

    Return the minimum maximum difference among all p pairs. We define the
    maximum of an empty set to be zero.
Link: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
Notes:
"""

import unittest


class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def count_pairs(threshold: int) -> int:
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            m = left + ((right - left) >> 1)
            if count_pairs(m) >= p:
                right = m
            else:
                left = m + 1
        return left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimizeMax1(self):
        n = [10, 1, 2, 7, 1, 3]
        p = 2
        expected = 1
        self.assertEqual(expected, self.sol.minimizeMax(n, p))

    def test_minimizeMax2(self):
        n = [4, 2, 1, 2]
        p = 1
        expected = 0
        self.assertEqual(expected, self.sol.minimizeMax(n, p))

    def test_minimizeMax3(self):
        n = [3, 4, 2, 3, 2, 1, 2]
        p = 3
        expected = 1
        self.assertEqual(expected, self.sol.minimizeMax(n, p))

    def test_minimizeMax4(self):
        n = [3, 3, 5, 1, 0, 5, 6, 6]
        p = 4
        expected = 1
        self.assertEqual(expected, self.sol.minimizeMax(n, p))


if __name__ == '__main__':
    unittest.main()
