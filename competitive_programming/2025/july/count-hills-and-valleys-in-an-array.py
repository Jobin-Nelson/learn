"""
Created Date: 2025-07-27
Qn: You are given a 0-indexed integer array nums. An index i is part of a hill
    in nums if the closest non-equal neighbors of i are smaller than nums[i].
    Similarly, an index i is part of a valley in nums if the closest non-equal
    neighbors of i are larger than nums[i]. Adjacent indices i and j are part
    of the same hill or valley if nums[i] == nums[j].

    Note that for an index to be part of a hill or valley, it must have a
    non-equal neighbor on both the left and right of the index.

    Return the number of hills and valleys in nums.
Link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
Notes:
    - store previous rising state and compare with current rising state
"""

import unittest
from itertools import groupby


class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        # Functional approach
        b = [v for v, _ in groupby(nums)]
        return sum(
            left < middle > right or left > middle < right
            for left, middle, right in zip(b, b[1:], b[2:])
        )

        # Imperative approach
        # hills = 0
        # vallies = 0
        # index = 1
        # while index < len(nums):
        #     if nums[index-1] != nums[index]:
        #         prev_is_rising = nums[index-1] < nums[index]
        #         break
        #     index += 1
        # else:
        #     return 0
        #
        #
        # for i in range(index, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         continue
        #     is_rising = nums[i - 1] < nums[i]
        #     if is_rising and not prev_is_rising:
        #         vallies += 1
        #     elif not is_rising and prev_is_rising:
        #         hills += 1
        #     prev_is_rising = is_rising
        # return vallies + hills


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countHillValley1(self):
        n = [2, 4, 1, 1, 6, 5]
        expected = 3
        self.assertEqual(expected, self.sol.countHillValley(n))

    def test_countHillValley2(self):
        n = [6, 6, 5, 5, 4, 1]
        expected = 0
        self.assertEqual(expected, self.sol.countHillValley(n))

    def test_countHillValley3(self):
        n = [1, 1, 1, 1, 1, 1, 1, 57, 57, 57, 50, 50, 50, 50, 22, 22, 22, 86]
        expected = 2
        self.assertEqual(expected, self.sol.countHillValley(n))


if __name__ == '__main__':
    unittest.main()
