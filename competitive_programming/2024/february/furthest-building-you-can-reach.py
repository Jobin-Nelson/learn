"""
Created Date: 2024-02-17
Qn: You are given an integer array heights representing the heights of
    buildings, some bricks, and some ladders.

    You start your journey from building 0 and move to the next building by
    possibly using bricks or ladders.

    While moving from building i to building i+1 (0-indexed),

        - If the current building's height is greater than or equal to the next
          building's height, you do not need a ladder or bricks. 
        - If the current building's height is less than the next building's
          height, you can either use one ladder or (h[i+1] - h[i]) bricks.

    Return the furthest building index (0-indexed) you can reach if you use the
    given ladders and bricks optimally.
Link: https://leetcode.com/problems/furthest-building-you-can-reach/
Notes:
    - use heap to keep track of the most largest difference
"""
import heapq

def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights)-1):
        diff = heights[i+1] - heights[i]
        if diff <= 0: continue
        bricks -= diff
        heapq.heappush(heap, -diff)
        if bricks < 0:
            if ladders == 0: return i
            ladders -= 1
            bricks += -heapq.heappop(heap)
    return len(heights)-1

if __name__ == '__main__':
    h1, b1, l1 = [4,2,7,6,9,14,12], 5, 1
    h2, b2, l2 = [4,12,2,7,3,18,20,3,19], 10, 2
    h3, b3, l3 = [14,3,19,3], 17, 0

    print(furthestBuilding(h1, b1, l1))
    print(furthestBuilding(h2, b2, l2))
    print(furthestBuilding(h3, b3, l3))
