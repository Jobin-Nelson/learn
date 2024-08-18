"""
Created Date: 2024-08-14
Qn: The distance of a pair of integers a and b is defined as the absolute
    difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest
    distance among all the pairs nums[i] and nums[j] where 0 <= i < j <
    nums.length.
Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
Notes:
    - use sort ,sliding window and binary search
"""


def smallestDistancePair(nums: list[int], k: int) -> int:
    nums.sort()

    def helper(i: int) -> int:
        l, res = 0, 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > i:
                l += 1
            res += r - l
        return res

    l, r = 0, max(nums)
    while l < r:
        m = l + ((r - l) >> 1)
        pairs = helper(m)
        if pairs >= k:
            r = m
        else:
            l = m + 1

    return l

    # TLE solution
    # N = len(nums)
    # heap = []
    #
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         diff = abs(nums[i] - nums[j])
    #         if len(heap) < k or heap[0] < diff:
    #             heapq.heappush(heap, -diff)
    #         if len(heap) > k:
    #             heapq.heappop(heap)
    # return -1 * heap[0]


if __name__ == '__main__':
    n1, k1 = [1, 3, 1], 1
    n2, k2 = [1, 1, 1], 2
    n3, k3 = [1, 6, 1], 3
    n4, k4 = [62, 100, 4], 2

    print(smallestDistancePair(n1, k1))
    print(smallestDistancePair(n2, k2))
    print(smallestDistancePair(n3, k3))
    print(smallestDistancePair(n4, k4))
