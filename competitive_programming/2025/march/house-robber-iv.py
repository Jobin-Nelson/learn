"""
Created Date: 2025-03-15
Qn: There are several consecutive houses along a street, each of which has some
    money inside. There is also a robber, who wants to steal money from the
    homes, but he refuses to steal from adjacent homes.

    The capability of the robber is the maximum amount of money he steals from
    one house of all the houses he robbed.

    You are given an integer array nums representing how much money is stashed
    in each house. More formally, the ith house from the left has nums[i]
    dollars.

    You are also given an integer k, representing the minimum number of houses
    the robber will steal from. It is always possible to steal at least k
    houses.

    Return the minimum capability of the robber out of all the possible ways to
    steal at least k houses.
Link: https://leetcode.com/problems/house-robber-iv/
Notes:
    - use binary search
"""

import unittest


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def is_valid(n: int) -> bool:
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= n:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        l, r = min(nums), max(nums)
        while l <= r:
            m = l + ((r - l) >> 1)
            if is_valid(m):
                r = m - 1
            else:
                l = m + 1
        return l


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minCapability1(self):
        n = [2, 3, 5, 9]
        k = 2
        expected = 5
        self.assertEqual(expected, self.sol.minCapability(n, k))

    def test_minCapability2(self):
        n = [2, 7, 9, 3, 1]
        k = 2
        expected = 2
        self.assertEqual(expected, self.sol.minCapability(n, k))


if __name__ == '__main__':
    unittest.main()
