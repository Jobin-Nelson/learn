"""
Created Date: 2024-05-11
Qn: There are n workers. You are given two integer arrays quality and wage
    where quality[i] is the quality of the ith worker and wage[i] is the
    minimum wage expectation for the ith worker.

    We want to hire exactly k workers to form a paid group. To hire a group of
    k workers, we must pay them according to the following rules:

        - Every worker in the paid group must be paid at least their minimum
          wage expectation. 
        - In the group, each worker's pay must be directly proportional to
          their quality. This means if a worker’s quality is double that of
          another worker in the group, then they must be paid twice as much as
          the other worker.

    Given the integer k, return the least amount of money needed to form a paid
    group satisfying the above conditions. Answers within 10-5 of the actual
    answer will be accepted.
Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
Notes:
"""
from sys import maxsize
import heapq

def minCostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:
    res = maxsize
    pairs = [(wage[i] / quality[i], quality[i]) for i in range(len(quality))]
    pairs.sort(key=lambda x: x[0])
    res = maxsize
    pairs = [(wage[i] / quality[i], quality[i]) for i in range(len(quality))]
    pairs.sort(key=lambda x: x[0])

    heap = []
    total_quantity=0
    for rate, q in pairs:
        heapq.heappush(heap, -q)
        total_quantity += q

        if len(heap) > k:
            total_quantity += heapq.heappop(heap)
        if len(heap) == k:
            res = min(
                res,
                total_quantity * rate
            )
    return res

    heap = []
    total_quantity=0
    for rate, q in pairs:
        heapq.heappush(heap, -q)
        total_quantity += q

        if len(heap) > k:
            total_quantity += heapq.heappop(heap)
        if len(heap) == k:
            res = min(
                res,
                total_quantity * rate
            )
    return res

if __name__ == '__main__':
    q1, w1, k1 = [10, 20, 5], [70, 50, 30], 2
    q2, w2, k2 = [3,1,10,10,1], [4,8,2,2,7], 3

    print(minCostToHireWorkers(q1, w1, k1))
    print(minCostToHireWorkers(q2, w2, k2))

