'''
Created Date: 2023-05-24
Qn: You are given two 0-indexed integer arrays nums1 and nums2 of equal length
    n and a positive integer k. You must choose a subsequence of indices from
    nums1 of length k.

    For chosen indices i0, i1, ..., ik - 1, your score is defined as:

        The sum of the selected elements from nums1 multiplied with the minimum
        of the selected elements from nums2. It can defined simply as:
        (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] ,
        nums2[i1], ... ,nums2[ik -
        1]).

    Return the maximum possible score.

    A subsequence of indices of an array is a set that can be derived from the
    set {0, 1, ..., n-1} by deleting some or no elements.
Link: https://leetcode.com/problems/maximum-subsequence-score/
Notes:
    - use heap to keep track of selected n1's
    - we only have to decide which n1 to remove from n1_sum
'''
import heapq
def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
    pairs.sort(key=lambda x: x[1], reverse=True)
    min_heap = []
    n1_sum = 0
    res = 0
    for n1, n2 in pairs:
        n1_sum += n1
        heapq.heappush(min_heap, n1)
        if len(min_heap) > k:
            n1_sum -= heapq.heappop(min_heap)

        if len(min_heap) == k:
            res = max(res, n1_sum * n2)
    return res

if __name__ == '__main__':
    n11, n12, k1 = [1,3,3,2], [2,1,3,4], 3
    n21, n22, k2 = [4,2,3,1,1], [7,5,10,9,6], 1

    print(maxScore(n11, n12, k1))
    print(maxScore(n21, n22, k2))
