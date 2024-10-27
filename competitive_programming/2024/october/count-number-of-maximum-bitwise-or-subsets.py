"""
Created Date: 2024-10-18
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
    - use dfs
"""


def countMaxOrSubsets(nums: list[int]) -> int:
    max_or = 0
    for n in nums:
        max_or |= n

    def dfs(i: int, cur_or: int) -> int:
        nonlocal max_or
        if i == len(nums):
            return 1 if cur_or == max_or else 0
        return dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])

    return dfs(0, 0)


if __name__ == '__main__':
    n1 = [3, 1]
    n2 = [2, 2, 2]
    n3 = [3, 2, 1, 5]

    print(countMaxOrSubsets(n1))
    print(countMaxOrSubsets(n2))
    print(countMaxOrSubsets(n3))
