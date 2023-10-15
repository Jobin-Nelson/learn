'''
Created Date: 2023-10-14
Qn: You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:

        - A paid painter that paints the ith wall in time[i] units of time and
          takes cost[i] units of money. 
        - A free painter that paints any wall in 1 unit of time at a cost of 0.
          But the free painter can only be used if the paid painter is already
          occupied.

    Return the minimum amount of money required to paint the n walls.
Link: https://leetcode.com/problems/painting-the-walls/
Notes:
'''
from functools import cache

def paintWalls(cost: list[int], time: list[int]) -> int:
    N = len(cost)
    @cache
    def dfs(i: int, remain: int) -> int:
        if remain <= 0: return 0
        if i == len(cost): return float('inf')
        paint = cost[i] + dfs(i+1, remain - 1 - time[i])
        skip = dfs(i+1, remain)
        return min(paint, skip)
    return dfs(0,N)

if __name__ == '__main__':
    c1, t1 = [1,2,3,2], [1,2,3,2]
    c2, t2 = [2,3,4,2], [1,1,1,1]
    print(paintWalls(c1, t1))
    print(paintWalls(c2, t2))
    
