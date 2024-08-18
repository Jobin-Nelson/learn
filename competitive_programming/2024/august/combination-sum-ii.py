"""
Created Date: 2024-08-13
Qn: Given a collection of candidate numbers (candidates) and a target number
    (target), find all unique combinations in candidates where the candidate
    numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.
Link: https://leetcode.com/problems/combination-sum-ii/
Notes:
    - use dfs
    - either include the current element or skip the element
"""


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates.sort()

    def dfs(i: int, cur_com: list[int], total: int) -> None:
        if total == target:
            res.append(cur_com.copy())
            return
        if total > target or i == len(candidates):
            return

        cur_com.append(candidates[i])
        dfs(i + 1, cur_com, total + candidates[i])
        cur_com.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, cur_com, total)

    dfs(0, [], 0)
    return res


if __name__ == '__main__':
    c1, t1 = [10, 1, 2, 7, 6, 1, 5], 8
    c2, t2 = [2, 5, 2, 1, 2], 5

    print(combinationSum2(c1, t1))
    print(combinationSum2(c2, t2))
