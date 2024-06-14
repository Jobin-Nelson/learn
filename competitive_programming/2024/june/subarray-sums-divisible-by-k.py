"""
Created Date: 2024-06-09
Qn: Given an integer array nums and an integer k, return the number of
    non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
Notes:
    - use prefix mod
"""
def subArrayDivByK(nums: list[int], k: int) -> int:
    remainders = [0] * k
    prefix_mod = 0
    res = 0

    remainders[0] = 1

    for n in nums:
        prefix_mod = (prefix_mod + n) % k
        res += remainders[prefix_mod]
        remainders[prefix_mod] += 1
    return res

if __name__ == '__main__':
    n1, k1 = [4,5,0,-2,-3,1], 5
    n2, k2 = [5], 9

    print(subArrayDivByK(n1, k1))
    print(subArrayDivByK(n2, k2))
