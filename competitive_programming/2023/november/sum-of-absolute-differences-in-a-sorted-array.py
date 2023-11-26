'''
Created Date: 2023-11-25
Qn: You are given an integer array nums sorted in non-decreasing order.

    Build and return an integer array result with the same length as nums such
    that result[i] is equal to the summation of absolute differences between
    nums[i] and all the other elements in the array.

    In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j <
    nums.length and j != i (0-indexed).
Link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
Notes:
    - use prefix sum
'''
def getSumAbsoluteDifference(nums: list[int]) -> list[int]:
    # nums[i] - nums[0] + nums[i] - nums[1] ... nums[i+1] - nums[i] nums[n-1] - nums[i]
    # (nums[i] * i - (nums[0] + nums[1] ... nums[i-1])) + ((nums[i+1] + nums[i+2] ... nums[n-1]) - nums[i] * (n-i-1))
    total = sum(nums)
    N = len(nums)
    left_sum = 0
    res = []

    for i in range(N):
        right_sum = total - left_sum - nums[i]
        res.append((nums[i] * i - left_sum) + (right_sum - nums[i] * (N-i-1)))
        left_sum += nums[i]
    return res

if __name__ == '__main__':
    n1 = [2,3,5]
    n2 = [1,4,6,8,10]

    print(getSumAbsoluteDifference(n1))
    print(getSumAbsoluteDifference(n2))
