"""
Created Date: 2024-06-24
Qn: You are given a binary array nums and an integer k.

    A k-bit flip is choosing a subarray of length k from nums and
    simultaneously changing every 0 in the subarray to 1, and every 1 in the
    subarray to 0.

    Return the minimum number of k-bit flips required so that there is no 0 in
    the array. If it is not possible, return -1.

    A subarray is a contiguous part of an array.
Link: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
Notes:
    - use queue or modify the nums in place
"""
from collections import deque

def minKBitFlips(nums: list[int], k: int) -> int:
    q = deque()
    res = 0
    for i in range(len(nums)):
        while q and i > q[0] + k - 1:
            q.popleft()
        if (nums[i] + len(q)) % 2 == 0:
            if i + k > len(nums):
                return -1
            res += 1
            q.append(i)
    return res

if __name__ == '__main__':
    n1, k1 = [0,1,0], 1
    n2, k2 = [1,1,0], 2
    n3, k3 = [0,0,0,1,0,1,1,0], 3

    print(minKBitFlips(n1, k1))
    print(minKBitFlips(n2, k2))
    print(minKBitFlips(n3, k3))
