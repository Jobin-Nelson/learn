"""
Created Date: 2024-06-08
Qn: Given an integer array nums and an integer k, return true if nums has a
    good subarray or false otherwise.

    A good subarray is a subarray where:

        - its length is at least two, and 
        - the sum of the elements of the subarray is a multiple of k.

    Note that:

        - A subarray is a contiguous part of the array. 
        - An integer x is a multiple of k if there exists an integer n such
          that x = n * k. 0 is always a multiple of k.

Link: https://leetcode.com/problems/continuous-subarray-sum/
Notes:
    - use prefix sum
"""
def checkSubarraySum(nums: list[int], k: int) -> bool:
    remainder = {0: -1}
    prefix_mod = 0
    for i, n in enumerate(nums):
        prefix_mod = (prefix_mod + n) % k
        if prefix_mod not in remainder:
            remainder[prefix_mod] = i
        elif i - remainder[prefix_mod] > 1:
            return True
    return False

if __name__ == '__main__':
    n1, k1 = [23, 2, 4, 6, 7], 6
    n2, k2 = [23, 2, 6, 4, 7], 6
    n3, k3 = [23, 2, 6, 4, 7], 13

    print(checkSubarraySum(n1, k1))
    print(checkSubarraySum(n2, k2))
    print(checkSubarraySum(n3, k3))
