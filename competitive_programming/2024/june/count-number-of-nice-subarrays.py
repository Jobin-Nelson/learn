"""
Created Date: 2024-06-22
Qn: Given an array of integers nums and an integer k. A continuous subarray is
    called nice if there are k odd numbers on it.

    Return the number of nice sub-arrays.
Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
Notes:
    - use 3 pointer sliding window
"""
def numberOfSubarrays(nums: list[int], k: int) -> int:
    res, odd = 0, 0
    l, m = 0, 0
    for r in range(len(nums)):
        if nums[r] & 1:
            odd += 1
        while odd > k:
            if nums[l] & 1:
                odd -= 1
            l += 1
            m = l
        if odd == k:
            while not nums[m] & 1:
                m += 1
            res += (m-l) + 1
    return res

if __name__ == '__main__':
    n1, k1 = [1,1,2,1,1], 3
    n2, k2 = [2,4,6], 1
    n3, k3 = [2,2,2,1,2,2,1,2,2,2], 2

    print(numberOfSubarrays(n1, k1))
    print(numberOfSubarrays(n2, k2))
    print(numberOfSubarrays(n3, k3))
