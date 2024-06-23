"""
Created Date: 2024-06-23
Qn: Given an array of integers nums and an integer limit, return the size of
    the longest non-empty subarray such that the absolute difference between
    any two elements of this subarray is less than or equal to limit.
Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
Notes:
    - use the sliding window
    - and use either heap or deques
"""
from collections import deque

def longestSubarray(nums: list[int], limit: int) -> int:
    # Deques
    max_deque = deque()
    min_deque = deque()
    l, res = 0, 0

    for r in range(len(nums)):
        # Maintain the max_deque in decreasing order
        while max_deque and max_deque[-1] < nums[r]:
            max_deque.pop()
        max_deque.append(nums[r])
        # Maintain the min_deque in increasing order
        while min_deque and min_deque[-1] > nums[r]:
            min_deque.pop()
        min_deque.append(nums[r])

        while max_deque[0] - min_deque[0] > limit:
            if max_deque[0] == nums[l]:
                max_deque.popleft()
            if min_deque[0] == nums[l]:
                min_deque.popleft()
            l += 1
        res = max(res, r - l + 1)
    return res


    # Heaps
    # min_heap, max_heap = [], []
    # l, res = 0, 0
    #
    # for r in range(len(nums)):
    #     heapq.heappush(max_heap, (-nums[r], r))
    #     heapq.heappush(min_heap, (nums[r], r))
    #
    #     while -max_heap[0][0] - min_heap[0][0] > limit:
    #         l = min(max_heap[0][1], min_heap[0][1]) + 1
    #         while max_heap[0][1] < l:
    #             heapq.heappop(max_heap)
    #         while min_heap[0][1] < l:
    #             heapq.heappop(min_heap)
    #     res = max(res, r - l + 1)
    # return res

if __name__ == '__main__':
    n1, l1 = [8,2,4,7], 4
    n2, l2 = [10,1,2,4,7,2], 5
    n3, l3 = [4,2,2,2,4,4,2,2], 0

    print(longestSubarray(n1, l1))
    print(longestSubarray(n2, l2))
    print(longestSubarray(n3, l3))

