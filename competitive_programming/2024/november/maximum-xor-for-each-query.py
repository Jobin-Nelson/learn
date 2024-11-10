"""
Created Date: 2024-11-08
Qn: You are given a sorted array nums of n non-negative integers and an integer
    maximumBit. You want to perform the following query n times:

    - Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1]
      XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to
      the ith query.
    - Remove the last element from the current array nums. Return an array
      answer, where answer[i] is the answer to the ith query.

Link: https://leetcode.com/problems/maximum-xor-for-each-query/
Notes:
    - use xor property of a ^ b = c, a ^ c = b
"""

import unittest
from functools import partial, reduce
from itertools import accumulate
from operator import xor


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        # Functional approach
        xor_all = reduce(xor, nums, 0)
        xors = accumulate(reversed(nums[1:]), xor, initial=xor_all)
        mask = (1 << maximumBit) - 1
        xor_mask = partial(xor, mask)
        return [xor_mask(x) for x in xors]

    
        # Imperative approach
        # for i in range(N):
        #     res[i] = xor_product ^ mask
        #     xor_product = xor_product ^ nums[N - i - 1]
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_getMaximumXor1(self):
        nums = [0, 1, 1, 3]
        mb = 2
        self.assertEqual(self.sol.getMaximumXor(nums, mb), [0, 3, 2, 3])

    def test_getMaximumXor2(self):
        nums = [2, 3, 4, 7]
        mb = 3
        self.assertEqual(self.sol.getMaximumXor(nums, mb), [5, 2, 6, 5])

    def test_getMaximumXor3(self):
        nums = [0, 1, 2, 2, 5, 7]
        mb = 3
        self.assertEqual(self.sol.getMaximumXor(nums, mb), [4, 3, 6, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
