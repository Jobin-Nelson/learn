"""
Created Date: 2025-04-28
Qn: The score of an array is defined as the product of its sum and its length.

    - For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 =
      75. Given a positive integer array nums and an integer k, return the
      number of non-empty subarrays of nums whose score is strictly less than
      k.

    A subarray is a contiguous sequence of elements within an array.
Link: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
Notes:
    - use two pointers
"""

import unittest


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        l = 0
        cur_sum = 0
        res = 0
        for r, n in enumerate(nums):
            cur_sum += n
            while l <= r and cur_sum * (r-l+1) >= k:
                cur_sum -= nums[l]
                l += 1
            res += (r-l+1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSubarrays1(self):
        n, k = [2,1,4,3,5], 10
        expected = 6
        self.assertEqual(expected, self.sol.countSubarrays(n, k))
    def test_countSubarrays2(self):
        n, k = [1,1,1], 5
        expected = 5
        self.assertEqual(expected, self.sol.countSubarrays(n, k))


if __name__ == '__main__':
    unittest.main()
