"""
Created Date: 2025-04-08
Qn: You are given an integer array nums. You need to ensure that the elements
    in the array are distinct. To achieve this, you can perform the following
    operation any number of times:

    - Remove 3 elements from the beginning of the array. If the array has fewer
      than 3 elements, remove all remaining elements.

    Note that an empty array is considered to have distinct elements. Return
    the minimum number of operations needed to make the elements in the array
    distinct.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
Notes:
"""

import unittest


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        N = len(nums)
        freq = [False] * 101
        for i in range(N - 1, -1, -1):
            if freq[nums[i]]:
                return i // 3 + 1
            freq[nums[i]] = True
        return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumOperations1(self):
        n = [1, 2, 3, 4, 2, 3, 3, 5, 7]
        expected = 2
        self.assertEqual(expected, self.sol.minimumOperations(n))

    def test_minimumOperations2(self):
        n = [4, 5, 6, 4, 4]
        expected = 2
        self.assertEqual(expected, self.sol.minimumOperations(n))

    def test_minimumOperations3(self):
        n = [6, 7, 8, 9]
        expected = 0
        self.assertEqual(expected, self.sol.minimumOperations(n))


if __name__ == '__main__':
    unittest.main()
