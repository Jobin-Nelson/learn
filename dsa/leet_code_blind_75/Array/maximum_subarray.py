'''
Qn: Given an integer array nums, find the contiguous subarray which has atleast one element which has the largest sum and return its sum
Link: https://leetcode.com/problems/maximum-subarray/
Notes:
- using two variables, one tracking sum of each subarrays that are positive, second tracking the max of sums of subarrays
'''

def max_subarray(nums):
    sum = nums[0]
    cur_sum = 0
    for i in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += nums[i]
        sum = cur_sum if cur_sum > sum else sum

    return sum

if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums1))