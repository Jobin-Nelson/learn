"""
Created Date: 2025-01-25
Qn: You are given a 0-indexed array of positive integers nums and a positive
    integer limit.

    In one operation, you can choose any two indices i and j and swap nums[i]
    and nums[j] if |nums[i] - nums[j]| <= limit.

    Return the lexicographically smallest array that can be obtained by
    performing the operation any number of times.

    An array a is lexicographically smaller than an array b if in the first
    position where a and b differ, array a has an element that is less than the
    corresponding element in b. For example, the array [2,10,3] is
    lexicographically smaller than the array [10,2,3] because they differ at
    index
    0 and 2 < 10.
Link: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
Notes:
"""

import unittest
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        groups = []
        num_to_groups = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_groups[n] = len(groups) - 1

        res = []
        for n in nums:
            j = num_to_groups[n]
            res.append(groups[j].popleft())
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lexicographicallySmallestArray1(self):
        n = [1, 5, 3, 9, 8]
        l = 2
        expected = [1, 3, 5, 8, 9]
        self.assertEqual(expected, self.sol.lexicographicallySmallestArray(n, l))

    def test_lexicographicallySmallestArray2(self):
        n = [1, 7, 6, 18, 2, 1]
        l = 3
        expected = [1, 6, 7, 18, 1, 2]
        self.assertEqual(expected, self.sol.lexicographicallySmallestArray(n, l))

    def test_lexicographicallySmallestArray3(self):
        n = [1, 7, 28, 19, 10]
        l = 3
        expected = [1, 7, 28, 19, 10]
        self.assertEqual(expected, self.sol.lexicographicallySmallestArray(n, l))


if __name__ == '__main__':
    unittest.main()
