'''
Created Date: 2023-04-24
Qn: You are given an array of integers stones where stones[i] is the weight of
    the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two
    stones and smash them together. Suppose the heaviest two stones have weights x
    and y with x <= y. The result of this smash is:

        - If x == y, both stones are destroyed, and 
        - If x != y, the stone of weight x is destroyed, and the stone of
          weight y has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left,
    return 0.
Link: https://leetcode.com/problems/last-stone-weight/
Notes:
    - use heapq
'''
import heapq

def lastStoneWeight(stones: list[int]) -> int:

    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        x = heapq.heappop(max_heap)
        y = heapq.heappop(max_heap)
        if x != y: heapq.heappush(max_heap, x-y)

    return -max_heap[0] if max_heap else 0

if __name__ == '__main__':
    s1 = [2,7,4,1,8,1]
    s2 = [1]

    print(lastStoneWeight(s1))
    print(lastStoneWeight(s2))
