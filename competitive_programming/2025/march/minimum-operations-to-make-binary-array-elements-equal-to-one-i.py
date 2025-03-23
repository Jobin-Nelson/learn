"""
Created Date: 2025-03-19
Qn: You are given a binary array nums.

    You can do the following operation on the array any number of times
    (possibly zero):

    - Choose any 3 consecutive elements from the array and flip all of them.
      Flipping an element means changing its value from 0 to 1, and from 1 to
      0.

    Return the minimum number of operations required to make all elements in
    nums
    equal to 1. If it is impossible, return -1.
Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
Notes:
    - use sliding window
    - use xor to flip
"""

import unittest


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] ^= 1
                count += 1
        return count if sum(nums) == len(nums) else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minOperations1(self):
        n = [0, 1, 1, 1, 0, 0]
        expected = 3
        self.assertEqual(expected, self.sol.minOperations(n))

    def test_minOperations2(self):
        n = [0, 1, 1, 1]
        expected = -1
        self.assertEqual(expected, self.sol.minOperations(n))


if __name__ == '__main__':
    unittest.main()
