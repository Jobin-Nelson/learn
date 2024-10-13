"""
Created Date: 2024-10-13
Qn: You have k lists of sorted integers in non-decreasing order. Find the
    smallest range that includes at least one number from each of the k lists.

    We define the range [a, b] is smaller than range [c, d] if b - a < d - c or
    a < c if b - a == d - c.
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
Notes:
    - use pointers for all the lists
"""

import heapq


def smallestRange(nums: list[list[int]]) -> list[int]:
    k = len(nums)

    left = right = nums[0][0]
    min_heap = []
    for i in range(k):
        l = nums[i]
        left = min(left, l[0])
        right = max(right, l[0])
        heapq.heappush(min_heap, (l[0], i, 0))  # num, idx of list, idx of n

    res = [left, right]
    while True:
        n, i, idx = heapq.heappop(min_heap)
        idx += 1
        if idx == len(nums[i]):
            break
        next_val = nums[i][idx]
        heapq.heappush(min_heap, (next_val, i, idx))
        right = max(right, next_val)
        left = min_heap[0][0]
        if right - left < res[1] - res[0]:
            res = [left, right]
    return res


if __name__ == '__main__':
    n1 = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    n2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

    print(smallestRange(n1))
    print(smallestRange(n2))
