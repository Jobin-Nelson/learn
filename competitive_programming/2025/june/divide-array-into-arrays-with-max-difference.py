"""
Created Date: 2025-06-18
Qn: You are given an integer array nums of size n where n is a multiple of 3
    and a positive integer k.

    Divide the array nums into n / 3 arrays of size 3 satisfying the following
    condition:

    - The difference between any two elements in one array is less than or
      equal to k.

    Return a 2D array containing the arrays. If it is impossible to satisfy the
    conditions, return an empty array. And if there are multiple answers,
    return any of them.
Link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
Notes:
    - sort and batch
"""

import unittest
from itertools import batched


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        res = []
        for n1, n2, n3 in batched(nums, 3):
            if n3 - n1 <= k:
                res.append([n1, n2, n3])
            else:
                return []
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_divideArray1(self):
        n = [1, 3, 4, 8, 7, 9, 3, 5, 1]
        k = 2
        expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
        self.assertEqual(expected, self.sol.divideArray(n, k))

    def test_divideArray2(self):
        n = [2, 4, 2, 2, 5, 2]
        k = 2
        expected = []
        self.assertEqual(expected, self.sol.divideArray(n, k))

    def test_divideArray3(self):
        n = [4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11]
        k = 14
        expected = [
            [2, 2, 12],
            [4, 8, 5],
            [5, 9, 7],
            [7, 8, 5],
            [5, 9, 10],
            [11, 12, 2],
        ]
        self.assertEqual(expected, self.sol.divideArray(n, k))


if __name__ == '__main__':
    unittest.main()
