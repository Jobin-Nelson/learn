"""
Created Date: 2024-12-07
Qn: You are given an integer array nums where the ith
    bag contains nums[i] balls. You are also given an
    integer maxOperations.

    You can perform the following operation at most
    maxOperations times:

    - Take any bag of balls and divide it into two
      new bags with a positive number of balls.
        - For example, a bag of 5 balls can become
          two new bags of 1 and 4 balls, or two new
          bags of 2 and 3 balls. Your penalty is the
          maximum number of balls in a bag. You want
          to minimize your penalty after the
          operations.

    Return the minimum possible penalty after
    performing the operations.
Link: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
Notes:
"""

import unittest
from itertools import accumulate
import math


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = l + ((r - l) >> 1)
            if self.is_possible(m, nums, maxOperations):
                r = m
            else:
                l = m + 1
        return l

    def is_possible(
        self, max_balls_in_bag: int, nums: list[int], maxOperations: int
    ) -> bool:
        # Functional approach
        operation = lambda x: math.ceil(x / max_balls_in_bag) - 1
        return all(op <= maxOperations for op in accumulate(map(operation, nums)))

        # Imperative approach
        # total_operations = 0
        # for num in nums:
        #     operations = math.ceil(num / max_balls_in_bag) -1
        #     total_operations += operations
        #     if total_operations > maxOperations:
        #         return False
        # return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumSize1(self):
        n = [9]
        m = 2
        expected = 3
        self.assertEqual(expected, self.sol.minimumSize(n, m))

    def test_minimumSize2(self):
        n = [2, 4, 8, 2]
        m = 4
        expected = 2
        self.assertEqual(expected, self.sol.minimumSize(n, m))


if __name__ == '__main__':
    unittest.main()
