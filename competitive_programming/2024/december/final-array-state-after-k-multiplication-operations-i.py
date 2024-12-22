"""
Created Date: 2024-12-16
Qn: You are given an integer array nums, an integer k, and an integer
    multiplier.

    You need to perform k operations on nums. In each operation:

    - Find the minimum value x in nums. If there are multiple occurrences of
      the minimum value, select the one that appears first.
    - Replace the selected minimum value x with x * multiplier.

    Return an integer array denoting the final state of nums after performing
    all k operations.
Link: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
Notes:
    - use heap
"""

import unittest
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            _, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))
        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_getFinalState1(self):
        n = [2,1,3,5,6]
        k = 5
        m = 2
        expected = [8,4,6,5,6]
        self.assertEqual(expected, self.sol.getFinalState(n,k,m))
    def test_getFinalState2(self):
        n = [1,2]
        k = 3
        m = 4
        expected = [16,8]
        self.assertEqual(expected, self.sol.getFinalState(n,k,m))


if __name__ == '__main__':
    unittest.main()
