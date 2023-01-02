'''
Created Date: 2022-12-28
Qn: You are given a 0-indexed integer array piles, where piles[i] represents
    the number of stones in the ith pile, and an integer k. You should apply
    the following operation exactly k times:

        - Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

    Notice that you can apply the operation on the same pile more than once.

    Return the minimum possible total number of stones remaining after applying
    the k operations.

    floor(x) is the greatest integer that is smaller than or equal to x 
    (i.e., rounds x down).
Link: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
Notes:
    - use heap
    - heap pop and push p - (p//2)
'''
import heapq
def minStoneSum(piles: list[int], k: int) -> int:
    hp = [-p for p in piles]
    heapq.heapify(hp)
    for _ in range(k):
        p = -heapq.heappop(hp)
        heapq.heappush(hp,-(p - (p // 2)))
    return -sum(hp)
if __name__ == '__main__':
    p1, k1 = [5, 4, 9], 2
    p2, k2 = [4, 3, 6, 7], 3

    print(minStoneSum(p1, k1))
    print(minStoneSum(p2, k2))
