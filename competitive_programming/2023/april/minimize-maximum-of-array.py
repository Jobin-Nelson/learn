'''
Created Date: 2023-04-05
Qn: You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:

    - Choose an integer i such that 1 <= i < n and nums[i] > 0. 
    - Decrease nums[i] by 1.
    - Increase nums[i - 1] by 1. 

    Return the minimum possible value of the maximum integer of nums after
    performing any number of operations.
Link: https://leetcode.com/problems/minimize-maximum-of-array/
Notes:
'''
def minimizeArrayValue(nums: list[int]) -> int:
    # my solution
    # N = len(nums)
    # if N == 1: return nums[0]
    # cur_max = nums[0]
    #
    # for i in range(1, N):
    #     while nums[i-1] < nums[i]:
    #         nums[i-1] += 1
    #         nums[i] -= 1
    #     cur_max = max(cur_max, nums[i])
    # return cur_max

    # more effecient solution
    res = cur_sum = 0

    for i in range(len(nums)):
        cur_sum += nums[i]
        res = max(res, (cur_sum + i) // (i + 1))
    return res

if __name__ == '__main__':
    n1 = [3,7,1,6]
    n2 = [10,1]

    print(minimizeArrayValue(n1))
    print(minimizeArrayValue(n2))
