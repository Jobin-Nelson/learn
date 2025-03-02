"""
Created Date: 2025-03-01
Qn: You are given a 0-indexed array nums of size n consisting of non-negative
    integers.

    You need to apply n - 1 operations to this array where, in the ith
    operation (0-indexed), you will apply the following on the ith element of
    nums:

    - If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1]
      to
      0. Otherwise, you skip this operation.

    After performing all the operations, shift all the 0's to the end of the
    array.

    - For example, the array [1,0,2,0,0,1] after shifting all its 0's to the
      end, is [1,2,1,0,0,0].

    Return the resulting array.

    Note that the operations are applied sequentially, not all at once.
Link: https://leetcode.com/problems/apply-operations-to-an-array/
Notes:
"""

import unittest
from itertools import accumulate


class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        # Functional approach
        N = len(nums)

        def count(a: tuple[int, int], b: int) -> tuple[int, int]:
            return (a[1] * 2, 0) if a[1] == b else (a[1], b)

        res = [
            n
            for n, _ in accumulate(nums[1:] + [0], count, initial=(0, nums[0]))
            if n != 0
        ]
        return res + ([0] * (N - len(res)))

        # Imperative approach
        # N = len(nums)
        # res = [0] * N
        # j = 0
        # for i in range(N-1):
        #     if nums[i] == nums[i+1]:
        #         nums[i] *= 2
        #         nums[i+1] = 0
        #     if nums[i] != 0:
        #         res[j] = nums[i]
        #         j += 1
        # res[j] = nums[-1]
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_applyOperations1(self):
        n = [1, 2, 2, 1, 1, 0]
        expected = [1, 4, 2, 0, 0, 0]
        self.assertEqual(expected, self.sol.applyOperations(n))

    def test_applyOperations2(self):
        n = [0, 1]
        expected = [1, 0]
        self.assertEqual(expected, self.sol.applyOperations(n))


if __name__ == '__main__':
    unittest.main()
