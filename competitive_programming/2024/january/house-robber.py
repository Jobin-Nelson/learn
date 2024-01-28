"""
Created Date: 2024-01-21
Qn: You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money stashed, the only constraint stopping
    you from robbing each of them is that adjacent houses have security systems
    connected and it will automatically contact the police if two adjacent
    houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the
    police.
Link: https://leetcode.com/problems/house-robber/
Notes:
    - use two variables to keep track of max of (n-2, n) or n-1
"""
def rob(nums: list[int]) -> int:
    r1, r2 = 0, 0
    for n in nums:
        r1, r2 = max(n + r2, r1), r1
    return r1

if __name__ == '__main__':
    n1 = [1,2,3,1]
    n2 = [2,7,9,3,1]

    print(rob(n1))
    print(rob(n2))
