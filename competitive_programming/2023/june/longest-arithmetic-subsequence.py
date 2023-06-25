'''
Created Date: 2023-06-23
Qn: Given an array nums of integers, return the length of the longest
    arithmetic subsequence in nums.

    Note that:

        - A subsequence is an array that can be derived from another array by
          deleting some or no elements without changing the order of the
          remaining elements. 
        - A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same
          value (for 0 <= i < seq.length - 1).

Link: https://leetcode.com/problems/longest-arithmetic-subsequence/
Notes:
    - use dp
'''
def longestArithSeqLength(nums: list[int]) -> int:
    dp = dict()

    for right in range(len(nums)):
        for left in range(right):
            dp[(right, nums[right]-nums[left])] = dp.get((left, nums[right]-nums[left]), 1) + 1
    return max(dp.values())

if __name__ == '__main__':
    n1 = [3,6,9,12]
    n2 = [9,4,7,2,10]
    n3 = [20,1,15,3,10,5,8]

    print(longestArithSeqLength(n1))
    print(longestArithSeqLength(n2))
    print(longestArithSeqLength(n3))
