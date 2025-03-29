"""
Created Date: 2025-03-27
Qn: An element x of an integer array arr of length m is dominant if more than
    half the elements of arr have a value of x.

    You are given a 0-indexed integer array nums of length n with one dominant
    element.

    You can split nums at an index i into two arrays nums[0, ..., i] and nums[i
    + 1, ..., n - 1], but the split is only valid if:

    - 0 <= i < n - 1
    - nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant
      element.

    Here, nums[i, ..., j] denotes the subarray of nums starting at index i and
    ending at index j, both ends being inclusive. Particularly, if j < i then
    nums[i, ..., j] denotes an empty subarray.

    Return the minimum index of a valid split. If no valid split exists, return
    -1.
Link: https://leetcode.com/problems/minimum-index-of-a-valid-split/
Notes:
    - majority algorithm
"""

import unittest


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        majority = 0
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1

        left = 0
        right = nums.count(majority)
        N = len(nums)

        for i, n in enumerate(nums):
            if n == majority:
                left += 1
                right -= 1
            left_len = i + 1
            right_len = N - left_len

            if 2 * left > left_len and 2 * right > right_len:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumIndex1(self):
        n = [1, 2, 2, 2]
        expected = 2
        self.assertEqual(expected, self.sol.minimumIndex(n))

    def test_minimumIndex2(self):
        n = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
        expected = 4
        self.assertEqual(expected, self.sol.minimumIndex(n))

    def test_minimumIndex3(self):
        n = [3, 3, 3, 3, 7, 2, 2]
        expected = -1
        self.assertEqual(expected, self.sol.minimumIndex(n))


if __name__ == '__main__':
    unittest.main()
