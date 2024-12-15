"""
Created Date: 2024-12-14
Qn: You are given a 0-indexed integer array nums. A subarray of nums is
    called continuous if:

    - Let i, i + 1, ..., j be the indices in the subarray. Then, for
      each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]|
      <= 2. Return the total number of continuous subarrays.

    A subarray is a contiguous non-empty sequence of elements within an
    array.
Link: https://leetcode.com/problems/continuous-subarrays/
Notes:
     - to count all subarrays in a window of length n, use `n*(n+1)//2`
"""

import unittest

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        l = r = 0
        res = window_len = 0

        cur_max = cur_min = nums[r]

        for r, n in enumerate(nums):
            cur_min = min(cur_min, n)
            cur_max = max(cur_max, n)
            if cur_max - cur_min > 2:
                window_len = r - l
                res += (window_len) * (window_len + 1) // 2

                l = r
                cur_max = cur_min = n
                while l > 0 and abs(nums[l - 1] - n) <= 2:
                    l -= 1
                    cur_min = min(cur_min, nums[l])
                    cur_max = max(cur_max, nums[l])

                if l < r:
                    window_len = r - l
                    res -= (window_len) * (window_len + 1) // 2

        window_len = r - l + 1
        res += (window_len) * (window_len + 1) // 2
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_continuousSubarrays1(self):
        n = [5, 4, 2, 4]
        expected = 8
        self.assertEqual(expected, self.sol.continuousSubarrays(n))

    def test_continuousSubarrays2(self):
        n = [1, 2, 3]
        expected = 6
        self.assertEqual(expected, self.sol.continuousSubarrays(n))


if __name__ == '__main__':
    unittest.main()
