"""
Created Date: 2025-02-02
Qn: Given an array nums, return true if the array was originally sorted in
    non-decreasing order, then rotated some number of positions (including
    zero). Otherwise, return false.

    There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an array B of the same
    length such that A[i] == B[(i+x) % A.length], where % is the modulo
    operation.
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Notes:
    - concatenate or mod to iterate over the same list twice
"""

import unittest
from itertools import accumulate, chain, pairwise


class Solution:
    def check(self, nums: list[int]) -> bool:
        # Functional approach
        N = len(nums)

        def count(acc: int, val: tuple[int, int]) -> int:
            return acc + 1 if val[0] <= val[1] else 1

        return N == 1 or any(
            v == N for v in accumulate(pairwise(chain(nums, nums)), count, initial=0)
        )

        # Imperative approach
        # N = len(nums)
        # count = 1
        # for i in range(1, 2*N):
        #     if nums[(i-1)%N] <= nums[i%N]:
        #         count += 1
        #     else:
        #         count = 1
        #     if count == N:
        #         return True
        # return N == 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_check1(self):
        n = [3, 4, 5, 1, 2]
        expected = True
        self.assertEqual(expected, self.sol.check(n))

    def test_check2(self):
        n = [2, 1, 3, 4]
        expected = False
        self.assertEqual(expected, self.sol.check(n))

    def test_check3(self):
        n = list(range(1, 4))
        expected = True
        self.assertEqual(expected, self.sol.check(n))


if __name__ == '__main__':
    unittest.main()
