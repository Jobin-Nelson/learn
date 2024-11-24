"""
Created Date: 2024-11-19
Qn: You are given an integer array nums and an integer k. Find the maximum
    subarray sum of all the subarrays of nums that meet the following
    conditions:

    - The length of the subarray is k, and
    - All the elements of the subarray are distinct.

    Return the maximum subarray sum of all the subarrays that meet the
    conditions. If no subarray meets the conditions, return 0.

    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
Notes:
    - use sliding window and hashmap num2index
"""

import unittest


class Solution:
    def maximumSubarray(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        cur_sum = 0
        res = 0
        num2ind = {}
        N = len(nums)
        while r < N:
            n = nums[r]
            last_ind = num2ind.get(n, -1)
            while l <= last_ind or r - l + 1 > k:
                cur_sum -= nums[l]
                l += 1
            num2ind[n] = r
            cur_sum += n
            if r - l + 1 == k:
                res = max(res, cur_sum)
            r += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumSubarray1(self):
        n, k = [1, 5, 4, 2, 9, 9, 9], 3
        self.assertEqual(self.sol.maximumSubarray(n, k), 15)

    def test_maximumSubarray2(self):
        n, k = [4, 4, 4], 3
        self.assertEqual(self.sol.maximumSubarray(n, k), 0)


if __name__ == '__main__':
    unittest.main()
