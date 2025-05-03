"""
Created Date: 2025-04-29
Qn: You are given an integer array nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at
    least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
Notes:
    - use sliding window
"""

import unittest


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_element = max(nums)
        res = l = count = 0

        for n in nums:
            if n == max_element:
                count += 1
            while count == k:
                if nums[l] == max_element:
                    count -= 1
                l += 1
            res += l
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSubarrays1(self):
        n, k = [1,3,2,3,3], 2
        expected = 6
        self.assertEqual(expected, self.sol.countSubarrays(n, k))

    def test_countSubarrays2(self):
        n, k = [1,3,2,3,3], 2
        expected = 6
        self.assertEqual(expected, self.sol.countSubarrays(n, k))

    def test_countSubarrays3(self):
        n, k = [1,4,2,1], 3
        expected = 0
        self.assertEqual(expected, self.sol.countSubarrays(n, k))


if __name__ == '__main__':
    unittest.main()
