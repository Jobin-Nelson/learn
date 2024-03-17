"""
Created Date: 2024-03-14
Qn: Given a binary array nums and an integer goal, return the number of
    non-empty subarrays with a sum goal.

    A subarray is a contiguous part of the array.
Link: https://leetcode.com/problems/binary-subarrays-with-sum/
Notes:
    - use sliding window
"""
def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    res = 0
    l = 0
    cur_sum = 0
    prefix_zeros = 0
    for r, n in enumerate(nums):
        cur_sum += n
        while l < r and (nums[l] == 0 or cur_sum > goal):
            if nums[l] == 1:
                prefix_zeros = 0
            else:
                prefix_zeros += 1
            cur_sum -= nums[l]
            l += 1
        if cur_sum == goal:
            res += 1 + prefix_zeros
    return res


if __name__ == '__main__':
    n1, g1 = [1,0,1,0,1], 2
    n2, g2 = [0] * 5, 0

    print(numSubarraysWithSum(n1, g1))
    print(numSubarraysWithSum(n2, g2))
