"""
Created Date: 2024-03-28
Qn: You are given an integer array nums and an integer k.

    The frequency of an element x is the number of times it occurs in an array.

    An array is called good if the frequency of each element in this array is
    less than or equal to k.

    Return the length of the longest good subarray of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
Notes:
    - use sliding window
"""
from collections import Counter

def maxSubarrayLength(nums: list[int], k: int) -> int:
    count = Counter()
    res = 0
    l = 0
    for r, n in enumerate(nums):
        count[n] += 1
        while count[n] > k:
            count[nums[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

if __name__ == '__main__':
    n1, k1 = [1,2,3,1,2,3,1,2], 2
    n2, k2 = [1,2,1,2,1,2,1,2], 1
    n3, k3 = [5,5,5,5,5,5,5], 4

    print(maxSubarrayLength(n1, k1))
    print(maxSubarrayLength(n2, k2))
    print(maxSubarrayLength(n3, k3))
