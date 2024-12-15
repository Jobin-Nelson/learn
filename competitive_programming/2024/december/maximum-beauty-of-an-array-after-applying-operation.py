"""
Created Date: 2024-12-11
Qn: You are given a 0-indexed array nums and a non-negative integer k.

    In one operation, you can do the following:

    - Choose an index i that hasn't been chosen before from the range [0,
      nums.length - 1].
    - Replace nums[i] with any integer from the range [nums[i] - k, nums[i] +
      k]. The beauty of the array is the length of the longest subsequence
      consisting of equal elements.

    Return the maximum possible beauty of the array nums after applying the
    operation any number of times.

    Note that you can apply the operation to each index only once.

    A subsequence of an array is a new array generated from the original array
    by deleting some elements (possibly none) without changing the order of the
    remaining elements.
Link: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
Notes:
    - sort and use sliding window approach
"""

import unittest


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 0
        l = 0
        for r, n in enumerate(nums):
            while n - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumBeauty1(self):
        n, k = [4, 6, 1, 2], 2
        expected = 3
        self.assertEqual(expected, self.sol.maximumBeauty(n, k))

    def test_maximumBeauty2(self):
        n, k = [1, 1, 1, 1], 10
        expected = 4
        self.assertEqual(expected, self.sol.maximumBeauty(n, k))


if __name__ == '__main__':
    unittest.main()
