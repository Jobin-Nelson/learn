"""
Created Date: 2025-04-07
Qn: Given an integer array nums, return true if you can partition the array
    into two subsets such that the sum of the elements in both subsets is equal
    or false otherwise.
Link: https://leetcode.com/problems/partition-equal-subset-sum/
Notes:
    use dp of dfs
"""

import unittest


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # DP
        if sum(nums) & 1:
            return False
        dp = set([0])
        target = sum(nums) >> 1
        for i in range(len(nums)-1, -1, -1):
            ndp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                ndp.add(t+nums[i])
                ndp.add(t)
            dp = ndp
        return target in dp
        # DFS
        # total = sum(nums)
        # def dfs(i: int, cur: int) -> bool:
        #     return cur == (total >> 1) or dfs(i+1, cur + nums[i]) or dfs(i+1, cur)
        # return (total & 1) == 0 and dfs(0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canPartition1(self):
        n = [1, 5, 11, 5]
        expected = True
        self.assertEqual(expected, self.sol.canPartition(n))

    def test_canPartition2(self):
        n = [1, 2, 3, 5]
        expected = False
        self.assertEqual(expected, self.sol.canPartition(n))


if __name__ == '__main__':
    unittest.main()
