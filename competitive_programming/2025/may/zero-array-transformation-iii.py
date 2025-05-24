"""
Created Date: 2025-05-22
Qn: You are given an integer array nums of length n and a 2D array queries
    where queries[i] = [li, ri].

    Each queries[i] represents the following action on nums:

    - Decrement the value at each index in the range [li, ri] in nums by at
      most 1.
    - The amount by which the value is decremented can be chosen independently
      for each index.

    A Zero Array is an array with all its elements equal to 0.

    Return the maximum number of elements that can be removed from queries,
    such that nums can still be converted to a zero array using the remaining
    queries.
If it is not possible to convert nums to a zero array, return -1.
Link: https://leetcode.com/problems/zero-array-transformation-iii/
Notes:
"""

import heapq
import unittest


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        queries.sort()
        heap = []

        delta_array = [0] * (len(nums) + 1)
        query_pos = 0
        applied_count = 0
        for i, n in enumerate(nums):
            applied_count += delta_array[i]
            while query_pos < len(queries) and queries[query_pos][0] == i:
                heapq.heappush(heap, -queries[query_pos][1])
                query_pos += 1

            while applied_count < n and heap and -heap[0] >= i:
                applied_count += 1
                delta_array[-heapq.heappop(heap) + 1] -= 1

            if applied_count < n:
                return -1

        return len(heap)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxRemoval1(self):
        n, q = [2, 0, 2], [[0, 2], [0, 2], [1, 1]]
        expected = 1
        self.assertEqual(expected, self.sol.maxRemoval(n, q))

    def test_maxRemoval2(self):
        n, q = [1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]
        expected = 2
        self.assertEqual(expected, self.sol.maxRemoval(n, q))

    def test_maxRemoval3(self):
        n, q = list(range(1, 5)), [[0, 3]]
        expected = -1
        self.assertEqual(expected, self.sol.maxRemoval(n, q))


if __name__ == '__main__':
    unittest.main()
