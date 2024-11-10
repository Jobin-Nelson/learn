"""
Created Date: 2024-11-10
Qn: You are given an array nums of non-negative integers and an integer k.

    An array is called special if the bitwise OR of all of its elements is
    at least k.

    Return the length of the shortest special non-empty subarray of nums,
    or return -1 if no special subarray exists.
Link: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
Notes:
    - use frequency table
"""

import unittest
from sys import maxsize
from functools import reduce


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        l, N = 0, len(nums)
        bits_freq = [0] * 32

        def get_or(freq: list[int]) -> int:
            # functional approach
            it = filter(lambda x: freq[x] > 0, range(32))
            return reduce(lambda x, y: x | (1 << y), it, 0)

            # b_or = 0
            # for i in range(32):
            #     if freq[i] > 0:
            #         b_or |= 1 << i
            # return b_or

        def add_bit(freq: list[int], num: int) -> None:
            for i in range(32):
                if (1 << i) & num:
                    freq[i] += 1

        def remove_bit(freq: list[int], num: int) -> None:
            for i in range(32):
                if (1 << i) & num:
                    freq[i] -= 1

        res = maxsize
        for r in range(N):
            add_bit(bits_freq, nums[r])
            cur_or = get_or(bits_freq)
            while l <= r and cur_or >= k:
                res = min(res, r - l + 1)
                remove_bit(bits_freq, nums[l])
                cur_or = get_or(bits_freq)
                l += 1
        return res if res != maxsize else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumSubarrayLength1(self):
        n, k = list(range(1, 4)), 2
        self.assertEqual(self.sol.minimumSubarrayLength(n, k), 1)

    def test_minimumSubarrayLength2(self):
        n, k = [2, 1, 8], 10
        self.assertEqual(self.sol.minimumSubarrayLength(n, k), 3)

    def test_minimumSubarrayLength3(self):
        n, k = [1, 2], 0
        self.assertEqual(self.sol.minimumSubarrayLength(n, k), 1)

    def test_minimumSubarrayLength4(self):
        n, k = [2, 1, 9, 12], 21
        self.assertEqual(self.sol.minimumSubarrayLength(n, k), -1)


if __name__ == '__main__':
    unittest.main()
