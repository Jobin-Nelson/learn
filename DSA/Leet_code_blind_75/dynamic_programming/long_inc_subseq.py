'''
Qn: Given an integer array nums, return the length of the longest strictly increasing subsequence.
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Notes:
- breaking the whole problem into subproblem and working from the bottom (last element) to the top (first element) 
- and incrementing the max only if the next number is greater than the current number
'''
def long_inc_subseq(nums: list[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums), -1, -1, -1):
        for j in range(i+1, len(nums)):
            if (nums[i]<nums[j]):
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

if __name__ == '__main__':
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = [0, 1, 0, 3, 2, 3]
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(long_inc_subseq(nums1))
    print(long_inc_subseq(nums2))
    print(long_inc_subseq(nums3))