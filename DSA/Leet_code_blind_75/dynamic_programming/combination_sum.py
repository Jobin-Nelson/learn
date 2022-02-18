'''
Qn: Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
Link: https://leetcode.com/problems/combination-sum-iv/
Notes:
- could be solved with both recursion and tabulation
- instantiate the numbers in the dp list and increment with num iteratively throughout dp
'''
def combination_sum_memo(nums, target):
    dp = [-1] * (target+1)
    dp[0] = 1
    if dp[target] > -1:
        return dp[target]
    res = 0
    for n in nums:
        if n <= target:
            res += combination_sum(nums, target-n)

    dp[target] = res
    return dp[target]

def combination_sum(nums, target):
    dp = [0] * (target+1)

    for n in nums:
        if n <= target:
            dp[n] = 1

    for i in range(target+1):
        for n in nums:
            if dp[i] > 0 and (i+n) <= target:
                dp[i+n] += dp[i] 
    return dp[target]

if __name__ == '__main__':
    nums1, target1 = [1, 2, 3], 4
    nums2, target2 = [9], 3
    print(combination_sum(nums1, target1))
    print(combination_sum(nums2, target2))
