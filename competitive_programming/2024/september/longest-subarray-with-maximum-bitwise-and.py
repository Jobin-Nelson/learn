"""
Created Date: 2024-09-14
Qn: You are given an integer array nums of size n.

    Consider a non-empty subarray from nums that has the maximum possible
    bitwise AND.

    In other words, let k be the maximum value of the bitwise AND of any
    subarray of nums. Then, only subarrays with a bitwise AND equal to k should
    be considered. Return the length of the longest such subarray.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A subarray is a contiguous sequence of elements within an array.
Link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
Notes:
    - count the number of contiguous max value
"""


def longestSubarray(nums: list[int]) -> int:
    max_val = res = cur = 0
    for n in nums:
        if max_val < n:
            max_val = n
            res = cur = 0
        if max_val == n:
            cur += 1
        else:
            cur = 0
        res = max(res, cur)
    return res


if __name__ == '__main__':
    n1 = [1, 2, 3, 3, 2, 2]
    n2 = list(range(1, 5))

    print(longestSubarray(n1))
    print(longestSubarray(n2))
