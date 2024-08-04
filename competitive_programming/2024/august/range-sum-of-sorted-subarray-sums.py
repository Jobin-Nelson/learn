"""
Created Date: 2024-08-04
Qn: You are given the array nums consisting of n positive integers. You
    computed the sum of all non-empty continuous subarrays from the array and
    then sorted them in non-decreasing order, creating a new array of n * (n +
    1) / 2 numbers.

    Return the sum of the numbers from index left to index right (indexed from
    1), inclusive, in the new array. Since the answer can be a huge number
    return it modulo 109 + 7.
Link: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
Notes:
    - use heapq
"""

import heapq


def rangeSum(nums: list[int], n: int, left: int, right: int) -> int:
    MOD = 10**9 + 7
    minHeap = [(n, i) for i, n in enumerate(nums)]
    heapq.heapify(minHeap)

    res = 0
    for i in range(right):
        num, index = heapq.heappop(minHeap)
        if i >= left - 1:
            res = (res + num) % MOD
        if index + 1 < n:
            next_pair = (num + nums[index + 1], index + 1)
            heapq.heappush(minHeap, next_pair)
    return res


if __name__ == '__main__':
    num1, n1, left1, right1 = list(range(1, 5)), 4, 1, 5
    num2, n2, left2, right2 = [1, 2, 3, 4], 4, 3, 4
    num3, n3, left3, right3 = list(range(1, 5)), 4, 1, 10

    print(rangeSum(num1, n1, left1, right1))
    print(rangeSum(num2, n2, left2, right2))
    print(rangeSum(num3, n3, left3, right3))
