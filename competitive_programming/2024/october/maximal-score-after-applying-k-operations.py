"""
Created Date: 2024-10-14
Qn: You are given a 0-indexed integer array nums and an integer k. You have a
    starting score of 0.

    In one operation:

    choose an index i such that 0 <= i < nums.length, increase your score by
    nums[i], and replace nums[i] with ceil(nums[i] / 3). Return the maximum
    possible score you can attain after applying exactly k operations.

    The ceiling function ceil(val) is the least integer greater than or equal
    to val.
Link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/
Notes:
    - use heap
"""

import heapq
import math


def maxKelements(nums: list[int], k: int) -> int:
    h = [-i for i in nums]
    heapq.heapify(h)
    res = 0
    for _ in range(k):
        score = -1 * heapq.heappop(h)
        res += score
        heapq.heappush(h, -1 * math.ceil(score / 3))
    return res


if __name__ == '__main__':
    n1, k1 = [10, 10, 10, 10, 10], 5
    n2, k2 = [1, 10, 3, 3, 3], 3

    print(maxKelements(n1, k1))
    print(maxKelements(n2, k2))
