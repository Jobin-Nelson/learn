"""
Created Date: 2024-08-18
Qn: An ugly number is a positive integer whose prime factors are limited to 2,
    3, and 5.

    Given an integer n, return the nth ugly number.
Link: https://leetcode.com/problems/ugly-number-ii/
Notes:
    - use heap or use 3 pointers to track 2, 3, and 5 factors
"""

import heapq


def nthUglyNumber(n: int) -> int:
    nums = [1]
    i2, i3, i5 = 0, 0, 0

    for i in range(1, n):
        next_num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
        nums.append(next_num)
        if next_num == nums[i2] * 2:
            i2 += 1
        if next_num == nums[i3] * 3:
            i3 += 1
        if next_num == nums[i5] * 5:
            i5 += 1
    return nums[n - 1]

    # heap = [1]
    # factors = [2, 3, 5]
    # visit = set()
    #
    # for _ in range(n - 1):
    #     num = heapq.heappop(heap)
    #     for f in factors:
    #         if num * f not in visit:
    #             visit.add(num * f)
    #             heapq.heappush(heap, num * f)
    # return heapq.heappop(heap)


if __name__ == '__main__':
    n1 = 10
    n2 = 1

    print(nthUglyNumber(n1))
    print(nthUglyNumber(n2))
