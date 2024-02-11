"""
Created Date: 2024-02-09
Qn: Given a set of distinct positive integers nums, return the largest subset
    answer such that every pair (answer[i], answer[j]) of elements in this
    subset satisfies:

        answer[i] % answer[j] == 0, or answer[j] % answer[i] == 0

    If there are multiple solutions, return any of them.
Link: https://leetcode.com/problems/largest-divisible-subset/
Notes:
    - use dfs and memoization
"""
def largestDivisibleSubset(nums: list[int]) -> list[int]:
    nums.sort()
    memo = {}
    def dfs(i: int, prev: int) -> list[int]:
        if i == len(nums): return []
        if (i, prev) in memo: return memo[(i, prev)]
        res = dfs(i+1, prev)
        if nums[i] % prev == 0:
            tmp = dfs(i+1, nums[i]) + [nums[i]]
            res = tmp if len(tmp) > len(res) else res
        memo[(i, prev)] = res
        return res
    return dfs(0, 1)

if __name__ == '__main__':
    n1 = [1,2,3]
    n2 = [1,2,4,8]

    print(largestDivisibleSubset(n1))
    print(largestDivisibleSubset(n2))
