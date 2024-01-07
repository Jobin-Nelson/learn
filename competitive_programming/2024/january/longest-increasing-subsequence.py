"""
Created Date: 2024-01-05
Qn: Given an integer array nums, return the length of the longest strictly
    increasing subsequence.
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Notes:
    - use dynamic programming
    - use binary search for O(n log n)
"""
from bisect import bisect_left
def lengthOfLIS(nums: list[int]) -> int:
    # binary search
    dp  = []
    for n in nums:
        id = bisect_left(dp, n)
        if id == len(dp):
            dp.append(n)
        else:
            dp[id] = n
    return len(dp)

    # dp
    # LIS = [1] * len(nums)
    #
    # for i in range(len(nums)-1, -1, -1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] < nums[j]:
    #             LIS[i] = max(LIS[i], 1 + LIS[j])
    # return max(LIS)

    # recursive
    # def dfs(i: int, max_till: int) -> int:
    #     if i == len(nums): return 0
    #     if max_till < nums[i]:
    #         return max(
    #             1 + dfs(i+1, nums[i]),
    #             dfs(i+1, max_till)
    #         )
    #     return dfs(i+1, max_till)
    # return dfs(0, float('-inf'))

if __name__ == '__main__':
    n1 = [10, 9, 2, 5, 3, 7, 101, 18]
    n2 = [0, 1, 0, 3, 2, 3]
    n3 = [7,7,7,7,7,7,7]

    print(lengthOfLIS(n1))
    print(lengthOfLIS(n2))
    print(lengthOfLIS(n3))
