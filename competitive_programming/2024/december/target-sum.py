"""
Created Date: 2024-12-26
Qn: You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols
    '+' and '-' before each integer in nums and then concatenate all the
    integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before
    1 and concatenate them to build the expression "+2-1". Return the number of
    different expressions that you can build, which evaluates to target.
Link: https://leetcode.com/problems/target-sum/
Notes:
"""

import unittest


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        dp[nums[0] + total_sum] = 1
        dp[-nums[0] + total_sum] += 1

        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp
        return 0 if abs(target) > total_sum else dp[target + total_sum]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findTargetSumWays1(self):
        n = [1] * 5
        t = 3
        expected = 5
        self.assertEqual(expected, self.sol.findTargetSumWays(n, t))

    def test_findTargetSumWays2(self):
        n = [1]
        t = 1
        expected = 1
        self.assertEqual(expected, self.sol.findTargetSumWays(n, t))


if __name__ == '__main__':
    unittest.main()
