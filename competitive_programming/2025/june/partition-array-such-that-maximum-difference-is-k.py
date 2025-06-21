"""
Created Date: 2025-06-19
Qn: You are given an integer array nums and an integer k. You may partition
    nums into one or more subsequences such that each element in nums appears
    in exactly one of the subsequences.

    Return the minimum number of subsequences needed such that the difference
    between the maximum and minimum values in each subsequence is at most k.

    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
Notes:
"""

import unittest


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        # Imperative
        nums.sort()
        rec = nums[0]
        res = 1
        for n in nums:
            if n - rec > k:
                res += 1
                rec = n
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_partitionArray1(self):
        n = [3, 6, 1, 2, 5]
        k = 2
        expected = 2
        self.assertEqual(expected, self.sol.partitionArray(n, k))

    def test_partitionArray2(self):
        n = [1, 2, 3]
        k = 1
        expected = 2
        self.assertEqual(expected, self.sol.partitionArray(n, k))

    def test_partitionArray3(self):
        n = [2, 2, 4, 5]
        k = 0
        expected = 3
        self.assertEqual(expected, self.sol.partitionArray(n, k))


if __name__ == '__main__':
    unittest.main()
