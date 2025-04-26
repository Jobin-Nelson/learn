"""
Created Date: 2025-04-24
Qn: You are given an array nums consisting of positive integers.

    We call a subarray of an array complete if the following condition is
    satisfied:

    - The number of distinct elements in the subarray is equal to the number of
      distinct elements in the whole array. Return the number of complete
      subarrays.

    A subarray is a contiguous non-empty part of an array.
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
Notes:
"""

import unittest


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        res = 0
        cnt = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))
        for left in range(n):
            if left > 0:
                remove = nums[left-1]
                cnt[remove] -= 1
                if cnt[remove] == 0:
                    cnt.pop(remove)
            while right < n and len(cnt) < distinct:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1
            if len(cnt) == distinct:
                res += n - right + 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countCompleteSubarrays1(self):
        n = [1, 3, 1, 2, 2]
        expected = 4
        self.assertEqual(expected, self.sol.countCompleteSubarrays(n))

    def test_countCompleteSubarrays2(self):
        n = [5, 5, 5, 5]
        expected = 10
        self.assertEqual(expected, self.sol.countCompleteSubarrays(n))


if __name__ == '__main__':
    unittest.main()
