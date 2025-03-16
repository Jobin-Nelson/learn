"""
Created Date: 2025-03-13
Qn: You are given an integer array nums of length n and a 2D array queries
    where queries[i] = [li, ri, vali].

    Each queries[i] represents the following action on nums:

    - Decrement the value at each index in the range [li, ri] in nums by at
      most vali.
    - The amount by which each value is decremented can be chosen independently
      for each index.

    A Zero Array is an array with all its elements equal to 0.

    Return the minimum possible non-negative value of k, such that after
    processing the first k queries in sequence, nums becomes a Zero Array. If
    no such k exists, return -1.
Link: https://leetcode.com/problems/zero-array-transformation-ii/
Notes:
    - use binary search
"""

import unittest
from itertools import accumulate


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        N = len(nums)
        left, right = 0, len(queries)

        def can_form_zero_array(k: int) -> bool:
            difference_array = [0] * (N + 1)
            for query_index in range(k):
                start, end, val = queries[query_index]
                difference_array[start] += val
                difference_array[end + 1] -= val

            return all(t >= n for t, n in zip(accumulate(difference_array), nums))

        if not can_form_zero_array(right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2
            if can_form_zero_array(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minZeroArray1(self):
        n = [2, 0, 2]
        q = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
        expected = 2
        self.assertEqual(expected, self.sol.minZeroArray(n, q))

    def test_minZeroArray2(self):
        n = [4, 3, 2, 1]
        q = [[1, 3, 2], [0, 2, 1]]
        expected = -1
        self.assertEqual(expected, self.sol.minZeroArray(n, q))


if __name__ == '__main__':
    unittest.main()
