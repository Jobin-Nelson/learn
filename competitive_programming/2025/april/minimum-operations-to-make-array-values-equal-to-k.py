"""
Created Date: 2025-04-09
Qn: You are given an integer array nums and an integer k.

    An integer h is called valid if all values in the array that are strictly
    greater than h are identical.

    For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all
    nums[i] > 9 are equal to 10, but 5 is not a valid integer.

    You are allowed to perform the following operation on nums:

    - Select an integer h that is valid for the current values in nums.
    - For each index i where nums[i] > h, set nums[i] to h.

    Return the minimum number of operations required to make every element in
    nums equal to k. If it is impossible to make all elements equal to k,
    return -1.
Link: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
Notes:
"""

import unittest


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return len(set(nums) | {k}) - 1 if min(nums) >= k else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minOperations1(self):
        n = [5, 2, 5, 4, 5]
        k = 2
        expected = 2
        self.assertEqual(expected, self.sol.minOperations(n, k))

    def test_minOperations2(self):
        n = [2, 1, 2]
        k = 2
        expected = -1
        self.assertEqual(expected, self.sol.minOperations(n, k))

    def test_minOperations3(self):
        n = [2, 1, 2]
        k = 2
        expected = -1
        self.assertEqual(expected, self.sol.minOperations(n, k))


if __name__ == '__main__':
    unittest.main()
