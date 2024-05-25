"""
Created Date: 2024-05-21
Qn: Given an integer array nums of unique elements, return all possible subsets
    (the power set).

    The solution set must not contain duplicate subsets. Return the solution in
    any order.
Link: https://leetcode.com/problems/subsets/
Notes:
    - use dfs or backtracking by modifying the same list
"""
from itertools import combinations

def subsets(nums: list[int]) -> list[list[int]]:
    # return [list(v) for i in range(len(nums)) for v in combinations(nums, i)]

    res = []
    def dfs(i: int, cur: list[int]):
        if i == len(nums):
            res.append(cur)
            return
        dfs(i+1, cur + [nums[i]])
        dfs(i+1, cur)
    dfs(0, [])
    return res

if __name__ == '__main__':
    n1 = [1, 2, 3]
    n2 = [0]

    print(subsets(n1))
    print(subsets(n2))
