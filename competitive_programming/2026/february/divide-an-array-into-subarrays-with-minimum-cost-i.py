"""
Created Date: 2026-02-01
Qn: You are given an array of integers nums of length n.

    The cost of an array is the value of its first element. For example, the
    cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

    You need to divide nums into 3 disjoint contiguous .

    Return the minimum possible sum of the cost of these subarrays.
Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
Notes:
"""

import unittest
from sys import maxsize


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        n1, n2, n3 = nums[0], maxsize, maxsize
        for n in nums[1:]:
            if n < n3:
                n2 = n3
                n3 = n
            elif n < n2:
                n2 = n
        return n1 + n2 + n3


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = [1, 2, 3, 12]
        expected = 6
        self.assertEqual(expected, self.sol.minimumCost(n))

    def test2(self):
        n = [5, 4, 3]
        expected = 12
        self.assertEqual(expected, self.sol.minimumCost(n))

    def test3(self):
        n = [10, 3, 1, 1]
        expected = 12
        self.assertEqual(expected, self.sol.minimumCost(n))


if __name__ == '__main__':
    unittest.main()
