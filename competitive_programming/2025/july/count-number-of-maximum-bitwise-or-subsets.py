"""
Created Date: 2025-07-28
Qn: Given an integer array nums, find the maximum possible bitwise OR of a
    subset of nums and return the number of different non-empty subsets with
    the maximum bitwise OR.

    An array a is a subset of an array b if a can be obtained from b by
    deleting some (possibly zero) elements of b. Two subsets are considered
    different if the indices of the elements chosen are different.

    The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length
    - 1] (0-indexed).
Link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
Notes:
    - use bitmask to iterate through 1<<16 solutions (worst case)
"""

import unittest


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n

        res = 0
        length = len(nums)
        for subset in range(1, 1 << length):
            cur_or = 0
            for i in range(length):
                if 1 << i & subset:
                    cur_or |= nums[i]
            if cur_or == max_or:
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countMaxOrSubsets1(self):
        n = [3, 1]
        expected = 2
        self.assertEqual(expected, self.sol.countMaxOrSubsets(n))

    def test_countMaxOrSubsets2(self):
        n = [2, 2, 2]
        expected = 7
        self.assertEqual(expected, self.sol.countMaxOrSubsets(n))

    def test_countMaxOrSubsets3(self):
        n = [3, 2, 1, 5]
        expected = 6
        self.assertEqual(expected, self.sol.countMaxOrSubsets(n))


if __name__ == '__main__':
    unittest.main()
