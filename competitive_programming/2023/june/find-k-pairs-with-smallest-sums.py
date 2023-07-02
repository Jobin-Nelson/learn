'''
Created Date: 2023-06-27
Qn: You are given two integer arrays nums1 and nums2 sorted in ascending order
    and an integer k.

    Define a pair (u, v) which consists of one element from the first array and
    one element from the second array.

    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest
    sums.
Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
Notes:
    - use heap
'''
import heapq
def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    res = []
    visited = set()
    N1, N2 = len(nums1), len(nums2)
    minHeap = [(nums1[0] + nums2[0], (0, 0))]
    visited.add((0, 0))

    while k > 0 and minHeap:
        val, (i, j) = heapq.heappop(minHeap)
        res.append([nums1[i], nums2[j]])
        if i+1 < N1 and (i+1, j) not in visited:
            heapq.heappush(minHeap, (nums1[i+1] + nums2[j], (i+1, j)))
            visited.add((i+1, j))
        if j+1 < N2 and (i, j+1) not in visited:
            heapq.heappush(minHeap, (nums1[i] + nums2[j+1], (i, j+1)))
            visited.add((i, j+1))
        k -= 1
    return res

if __name__ == '__main__':
    n11, n12, k1 = [1,7,11], [2,4,6], 3
    n21, n22, k2 = [1,1,2], [1,2,3], 2
    n31, n32, k3 = [1,2], [3], 3

    print(kSmallestPairs(n11, n12, k1))
    print(kSmallestPairs(n21, n22, k2))
    print(kSmallestPairs(n31, n32, k3))
