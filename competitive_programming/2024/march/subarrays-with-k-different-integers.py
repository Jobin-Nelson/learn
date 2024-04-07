"""
Created Date: 2024-03-30
Qn: Given an integer array nums and an integer k, return the number of good
    subarrays of nums.

    A good array is an array where the number of different integers in that
    array is exactly k.

        For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/subarrays-with-k-different-integers/
Notes:
    - use 3 pointers sliding window
"""
from collections import defaultdict

def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    res = 0
    lf = ln = r = 0

    for r in range(len(nums)):
        count[nums[r]] += 1
        while len(count) > k:
            count[nums[ln]] -= 1
            if count[nums[ln]] == 0:
                count.pop(nums[ln])
            ln += 1
            lf = ln

        while count[nums[ln]] > 1:
            count[nums[ln]] -=1 
            ln += 1
        if len(count) == k:
            res += ln - lf + 1
    return res
    # distinct_count = defaultdict(int)
    # total_count = 0
    # curr_count = 0
    # left = right = 0
    #
    # while right < len(nums):
    #     distinct_count[nums[right]] += 1
    #
    #     if distinct_count[nums[right]] == 1:
    #         k -= 1
    #
    #     if k < 0:
    #         distinct_count[nums[left]] -= 1
    #         if distinct_count[nums[left]] == 0:
    #             k += 1
    #         left += 1
    #         curr_count = 0
    #
    #     if k == 0:
    #         while distinct_count[nums[left]] > 1:
    #             distinct_count[nums[left]] -= 1
    #             left += 1
    #             curr_count += 1
    #         total_count += curr_count
    #     right += 1
    #
    # return total_count

if __name__ == '__main__':
    n1, k1 = [1,2,1,2,3], 2
    n2, k2 = [1,2,1,3,4], 3

    print(subarraysWithKDistinct(n1, k1))
    print(subarraysWithKDistinct(n2, k2))
