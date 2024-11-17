"""
Created Date: 2024-11-17
Qn: Given an integer array nums and an integer k, return the length of the
    shortest non-empty subarray of nums with a sum of at least k. If there is
    no such subarray, return -1.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Notes:
    - use monotonic increasing stack
"""

import unittest
from sys import maxsize
from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int):
        q = deque()
        res = maxsize
        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum >= k:
                res = min(res, i + 1)
            while q and cur_sum - q[0][0] >= k:
                _prefix, end_idx = q.popleft()
                res = min(res, i-end_idx)
            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum, i))
        return res if res != maxsize else -1
                

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shortestSubarray1(self):
        n, k = [1], 1
        self.assertEqual(self.sol.shortestSubarray(n, k), 1)

    def test_shortestSubarray2(self):
        n, k = [1, 2], 4
        self.assertEqual(self.sol.shortestSubarray(n, k), -1)

    def test_shortestSubarray3(self):
        n, k = [2, -1, 2], 3
        self.assertEqual(self.sol.shortestSubarray(n, k), 3)

    def test_shortestSubarray4(self):
        n, k = [84,-37,32,40,95], 167
        self.assertEqual(self.sol.shortestSubarray(n, k), 3)


if __name__ == '__main__':
    unittest.main()
