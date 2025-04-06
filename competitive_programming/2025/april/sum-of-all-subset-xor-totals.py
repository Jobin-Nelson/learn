"""
Created Date: 2025-04-05
Qn: The XOR total of an array is defined as the bitwise XOR of all its
    elements, or 0 if the array is empty.

    - For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
      Given an array nums, return the sum of all XOR totals for every subset of
      nums.

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by
    deleting some (possibly zero) elements of b.
Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Notes:
"""

import unittest


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def XOR_sum(nums: list[int], index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor

            with_element = XOR_sum(nums, index + 1, current_xor ^ nums[index])
            without_element = XOR_sum(nums, index + 1, current_xor)
            return with_element + without_element

        return XOR_sum(nums, 0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_subsetXORSum1(self):
        n = [1, 3]
        expected = 6
        self.assertEqual(expected, self.sol.subsetXORSum(n))

    def test_subsetXORSum2(self):
        n = [5, 1, 6]
        expected = 28
        self.assertEqual(expected, self.sol.subsetXORSum(n))

    def test_subsetXORSum3(self):
        n = [3, 4, 5, 6, 7, 8]
        expected = 480
        self.assertEqual(expected, self.sol.subsetXORSum(n))


if __name__ == '__main__':
    unittest.main()
