"""
Created Date: 2025-02-13
Qn: You are given a 0-indexed integer array nums, and an integer k.

    In one operation, you will:

    - Take the two smallest integers x and y in nums.
    - Remove x and y from nums.
    - Add min(x, y) * 2 + max(x, y) anywhere in the array.

    Note that you can only apply the described operation if nums contains at
    least two elements.

    Return the minimum number of operations needed so that all elements of the
    array are greater than or equal to k.
Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
Notes:
    - use heap
"""

import unittest
import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        steps = 0
        while nums[0] < k:
            if len(nums) < 2:
                return -1
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            heapq.heappush(nums, min(a, b) * 2 + max(a, b))
            steps += 1
        return steps


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minOperations1(self):
        n = [2, 11, 10, 1, 3]
        k = 10
        expected = 2
        self.assertEqual(expected, self.sol.minOperations(n, k))

    def test_minOperations2(self):
        n = [1, 1, 2, 4, 9]
        k = 20
        expected = 4
        self.assertEqual(expected, self.sol.minOperations(n, k))


if __name__ == '__main__':
    unittest.main()
