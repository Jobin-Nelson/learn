"""
Created Date: 2025-07-29
Qn: You are given a 0-indexed array nums of length n, consisting of
    non-negative integers. For each index i from 0 to n - 1, you must determine
    the size of the minimum sized non-empty subarray of nums starting at i
    (inclusive) that has the maximum possible bitwise OR.

    - In other words, let Bij be the bitwise OR of the subarray nums[i...j].
      You need to find the smallest subarray starting at i, such that bitwise
      OR of this subarray is equal to max(Bik) where i <= k <= n - 1.

    The bitwise OR of an array is the bitwise OR of all the numbers in it.

    Return an integer array answer of size n where answer[i] is the length of
    the minimum sized subarray starting at i with maximum bitwise OR.

    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
Notes:
    - iterate from right to left and track nearest bitset
"""

import unittest


class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pos = [-1] * 31
        res = [0] * n

        for i in range(n-1, -1, -1):
            j = i
            for bit in range(31):
                if nums[i] & (1 << bit) == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                else:
                    pos[bit] = i
            res[i] = j - i + 1
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_smallestSubarrays1(self):
        n = [1, 0, 2, 1, 3]
        expected = [3, 3, 2, 2, 1]
        self.assertEqual(expected, self.sol.smallestSubarrays(n))

    def test_smallestSubarrays2(self):
        n = [1, 2]
        expected = [2, 1]
        self.assertEqual(expected, self.sol.smallestSubarrays(n))


if __name__ == '__main__':
    unittest.main()
