"""
Created Date: 2024-10-03
Qn: Given an array of positive integers nums, remove the smallest subarray
    (possibly empty) such that the sum of the remaining elements is divisible
    by p. It is not allowed to remove the whole array.

    Return the length of the smallest subarray that you need to remove, or -1
    if it's impossible.

    A subarray is defined as a contiguous block of elements in the array.
Link: https://leetcode.com/problems/make-sum-divisible-by-p/
Notes:
    - use prefix sum
"""


def minSubarray(nums: list[int], p: int) -> int:
    total = sum(nums)
    rem = total % p
    if rem == 0:
        return 0
    n = len(nums)
    min_len = n
    cur_total = 0
    mod_map = {0: -1}

    for i in range(n):
        cur_total = (cur_total + nums[i]) % p
        needed = (cur_total - rem + p) % p
        if needed in mod_map:
            min_len = min(min_len, i - mod_map[needed])
        mod_map[cur_total] = i
    return -1 if min_len == n else min_len


if __name__ == '__main__':
    n1, p1 = [3, 1, 4, 2], 6
    n2, p2 = [6, 3, 5, 2], 9
    n3, p3 = [1, 2, 3], 3

    print(minSubarray(n1, p1))
    print(minSubarray(n2, p2))
    print(minSubarray(n3, p3))
