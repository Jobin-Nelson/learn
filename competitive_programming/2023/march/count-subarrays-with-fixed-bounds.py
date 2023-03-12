'''
Created Date: 2023-03-04
Qn: You are given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following
    conditions:

        - The minimum value in the subarray is equal to minK.
        - The maximum value in the subarray is equal to maxK.

    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
Notes:
    - use two pointers
'''
def countSubarrays(nums: list[int], minK: int, maxK: int) -> int:
    res = 0
    leftBound = -1
    lastMin, lastMax = -1, -1

    for i in range(len(nums)):
        if nums[i] >= minK and nums[i] <= maxK:
            if nums[i] == minK: lastMin = i
            if nums[i] == maxK: lastMax = i
            res += max(0, min(lastMin, lastMax) - leftBound)
        else:
            leftBound = i
            lastMin = -1
            lastMax = -1
    return res

if __name__ == '__main__':
    n1, minK1, maxK1 = [1,3,5,2,7,5], 1, 5
    n2, minK2, maxK2 = [1,1,1,1], 1, 1

    print(countSubarrays(n1, minK1, maxK1))
    print(countSubarrays(n2, minK2, maxK2))
