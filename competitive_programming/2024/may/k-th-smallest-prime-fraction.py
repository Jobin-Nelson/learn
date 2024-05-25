"""
Created Date: 2024-05-10
Qn: You are given a sorted integer array arr containing 1 and prime numbers,
    where all the integers of arr are unique. You are also given an integer k.

    For every i and j where 0 <= i < j < arr.length, we consider the fraction
    arr[i] / arr[j].

    Return the kth smallest fraction considered. Return your answer as an array
    of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
Link: https://leetcode.com/problems/k-th-smallest-prime-fraction/
Notes:
    - use min heap or binary search
"""
import heapq

def kthSmallestPrimeFraction(arr: list[int], k: int) -> list[int]:
    N = len(arr)
    heap = []

    for i in range(N):
        heapq.heappush(heap, (arr[i] / arr[-1], i, N-1))

    for _ in range(k-1):
        cur = heapq.heappop(heap)
        numerator_index = cur[1]
        denominator_index = cur[2] - 1
        if denominator_index > numerator_index:
            heapq.heappush(heap, (
                arr[numerator_index] / arr[denominator_index],
                numerator_index,
                denominator_index
            ))
    res = heapq.heappop(heap)
    return [arr[res[1]], arr[res[2]]]

if __name__ == '__main__':
    a1, k1 = [1,2,3,5], 3
    a2, k2 = [1,7], 1

    print(kthSmallestPrimeFraction(a1, k1))
    print(kthSmallestPrimeFraction(a2, k2))
