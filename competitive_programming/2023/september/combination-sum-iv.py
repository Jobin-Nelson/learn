'''
Created Date: 2023-09-09
Qn: Given an array of distinct integers nums and a target integer target,
    return the number of possible combinations that add up to target.

    The test cases are generated so that the answer can fit in a 32-bit
    integer.
Link: https://leetcode.com/problems/combination-sum-iv/
Notes:
    - can be solved using dfs or bottom-up dp
'''
def combinationSum4(nums: list[int], target: int) -> int:
    # bottom-up dp
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for n in nums:
            if i - n >= 0: dp[i] += dp[i-n]
    return dp[target]
            
    # dfs
    # res = 0
    # def dfs(cur_sum: int) -> None:
    #     if cur_sum > target: return
    #     nonlocal res
    #     if cur_sum == target: res += 1
    #     for n in nums:
    #         dfs(cur_sum + n)
    # dfs(0)
    # return res

if __name__ == '__main__':
    n1, t1 = [1,2,3], 4
    n2, t2 = [9], 3

    print(combinationSum4(n1, t1))
    print(combinationSum4(n2, t2))
