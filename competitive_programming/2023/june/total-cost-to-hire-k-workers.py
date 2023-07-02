'''
Created Date: 2023-06-26
Qn: You are given a 0-indexed integer array costs where costs[i] is the cost of
    hiring the ith worker.

    You are also given two integers k and candidates. We want to hire exactly k
    workers according to the following rules:

        - You will run k sessions and hire exactly one worker in each session. 
        - In each hiring session, choose the worker with the lowest cost from
          either the first candidates workers or the last candidates workers.
          Break the tie by the smallest index. 
            - For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in
              the first hiring session, we will choose the 4th worker because
              they have the lowest cost [3,2,7,7,1,2]. 
            - In the second hiring session, we will choose 1st worker because
              they have the same lowest cost as 4th worker but they have the
              smallest index [3,2,7,7,2]. Please note that the indexing may be
              changed in the process. 
        - If there are fewer than candidates workers remaining, choose the
          worker with the lowest cost among them. Break the tie by the smallest
          index. 
        - A worker can only be chosen once.

    Return the total cost to hire exactly k workers.
Link: https://leetcode.com/problems/total-cost-to-hire-k-workers/
Notes:
    - use heap
'''
import heapq

def totalCost(costs: list[int], k: int, candidates: int) -> int:
    head_workers = costs[:candidates]
    tail_workers = costs[max(candidates, len(costs) - candidates):]
    heapq.heapify(head_workers)
    heapq.heapify(tail_workers)

    res = 0
    next_head, next_tail = candidates, len(costs) - 1 - candidates

    for _ in range(k):
        if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
            res += heapq.heappop(head_workers)

            if next_head <= next_tail:
                heapq.heappush(head_workers, costs[next_head])
                next_head += 1
        else:
            res += heapq.heappop(tail_workers)

            if next_head <= next_tail:
                heapq.heappush(tail_workers, costs[next_tail])
                next_tail -= 1
    return res

if __name__ == '__main__':
    c1, k1, ca1 = [17,12,10,2,7,2,11,20,8], 3, 4
    c2, k2, ca2 = [1,2,4,1], 3, 3

    print(totalCost(c1, k1, ca1))
    print(totalCost(c2, k2, ca2))
