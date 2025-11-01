"""
Created Date: 2025-10-28
Qn: You are given an integer array nums.

    Start by selecting a starting position curr such that nums[curr] == 0, and
    choose a movement direction of either left or right.

    After that, you repeat the following process:

    - If curr is out of the range [0, n - 1], this process ends.
    - If nums[curr] == 0, move in the current direction by incrementing curr if
      you are moving right, or decrementing curr if you are moving left.
    - Else if nums[curr] > 0:
        - Decrement nums[curr] by 1.
        - Reverse your movement direction (left becomes right and vice versa).
        - Take a step in your new direction.

    A selection of the initial position curr and movement direction is
    considered valid if every element in nums becomes 0 by the end of the
    process.

    Return the number of possible valid selections.
Link: https://leetcode.com/problems/make-array-elements-equal-to-zero/
Notes:
"""

import unittest


class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        res = 0
        left, right = 0, sum(nums)

        for n in nums:
            if n == 0:
                if 0 <= left - right <= 1:
                    res += 1
                if 0 <= right - left <= 1:
                    res += 1
            else:
                left += n
                right -= n
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()
