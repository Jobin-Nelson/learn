"""
Created Date: 2024-11-06
Qn: You are given a 0-indexed array of positive integers nums.

    In one operation, you can swap any two adjacent elements if they have the
    same number of set bits . You are allowed to do this operation any number
    of times (including zero).

    Return true if you can sort the array, else return false.
Link: https://leetcode.com/problems/find-if-array-can-be-sorted/
Notes:
    - compare groups with same bit set
    - if we prev group max is not less than cur group min then return false
"""

import unittest


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        cur_min, cur_max = nums[0], nums[0]
        prev_max = float('-inf')

        for n in nums:
            if n.bit_count() == cur_min.bit_count():
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min, cur_max = n, n
        return cur_min > prev_max

        # snums = sorted(nums)
        #
        # for n, sn in zip(nums, snums):
        #     if n.bit_count() != sn.bit_count():
        #         return False
        # return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canSortArray1(self):
        n = [8,4,2,30,15]
        self.assertEqual(self.sol.canSortArray(n), True)
    def test_canSortArray2(self):
        n = list(range(1,6))
        self.assertEqual(self.sol.canSortArray(n), True)
    def test_canSortArray3(self):
        n = [3,16,8,4,2]
        self.assertEqual(self.sol.canSortArray(n), False)


if __name__ == '__main__':
    unittest.main()
