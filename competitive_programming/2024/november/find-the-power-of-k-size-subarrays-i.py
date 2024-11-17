"""
Created Date: 2024-11-16
Qn: You are given an array of integers nums of length n and a positive integer
    k.

    The power of an array is defined as:

    - Its maximum element if all of its elements are consecutive and sorted in
      ascending order.
    - -1 otherwise.

    You need to find the power of all subarrays of nums of size k.

    Return an integer array results of size n - k + 1, where results[i] is the
    power of nums[i..(i + k - 1)].
Link: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
Notes:
    - use sliding window
"""

import unittest


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        l = 0
        res = []
        consec_count = 1
        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                consec_count += 1
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    consec_count -= 1
                l += 1
            if r - l + 1 == k:
                res.append(nums[r] if consec_count == k else -1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_resultsArray1(self):
        nums, k = [1, 2, 3, 4, 3, 2, 5], 3
        expected = [3, 4, -1, -1, -1]
        self.assertEqual(self.sol.resultsArray(nums, k), expected)

    def test_resultsArray2(self):
        nums, k = [2] * 5, 4
        expected = [-1, -1]
        self.assertEqual(self.sol.resultsArray(nums, k), expected)

    def test_resultsArray3(self):
        nums, k = [3, 2] * 3, 2
        expected = [-1, 3, -1, 3, -1]
        self.assertEqual(self.sol.resultsArray(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
