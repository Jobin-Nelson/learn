"""
Created Date: 2025-02-12
Qn: You are given a 0-indexed array nums consisting of positive integers. You
    can choose two indices i and j, such that i != j, and the sum of digits of
    the number nums[i] is equal to that of nums[j].

    Return the maximum value of nums[i] + nums[j] that you can obtain over all
    possible indices i and j that satisfy the conditions.
Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
Notes:
    - use hashmap to store the sum till now
"""

import unittest


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        sums = {}
        res = -1

        def digit_sum(num: int) -> int:
            res = 0
            cur = num
            while cur:
                res += cur % 10
                cur //= 10
            return res

        for n in nums:
            cur_sum = digit_sum(n)
            if cur_sum in sums:
                res = max(res, sums[cur_sum] + n)
                sums[cur_sum] = max(sums[cur_sum], n)
            else:
                sums[cur_sum] = n
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumSum1(self):
        n = [18, 43, 36, 13, 7]
        expected = 54
        self.assertEqual(expected, self.sol.maximumSum(n))

    def test_maximumSum2(self):
        n = [10, 12, 19, 14]
        expected = -1
        self.assertEqual(expected, self.sol.maximumSum(n))


if __name__ == '__main__':
    unittest.main()
