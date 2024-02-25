"""
Created Date: 2024-02-23
Qn: There are n cities connected by some number of flights. You are given an
    array flights where flights[i] = [fromi, toi, pricei] indicates that there
    is a flight from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest
    price from src to dst with at most k stops. If there is no such route,
    return -1.
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Notes:
    - Bellman Ford algorithm
"""
import heapq
from sys import maxsize

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    grid = [[] for _ in range(n)]
    for frm, to, cst in flights:
        grid[frm].append((cst, to))

    st: list[tuple[int, int, int]] = [(0, 0, src)]
    css = [(maxsize, maxsize)] * n
    css[src] = (0, 0)
    while st:
        cst, stop, x = heapq.heappop(st)
        if x == dst: return cst
        if stop <= k:
            for ct, to in grid[x]:
                if css[to][0]>ct+cst or css[to][1]>stop+1:
                    css[to] = (ct+cst, stop+1)
                    heapq.heappush(st, (ct+cst, stop+1, to))
    return -1

    # prices = [float('inf')] * n
    # prices[src] = 0
    #
    # for i in range(k+1):
    #     tmpPrices = prices.copy()
    #     for s, d, p in flights:
    #         if prices[s] == float('inf'): continue
    #         if prices[s] + p < tmpPrices[d]:
    #             tmpPrices[d] = prices[s] + p
    #     prices = tmpPrices
    # return -1 if prices[dst] == float('inf') else prices[dst]



if __name__ == '__main__':
    n1, f1, s1, d1, k1 = 4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1
    n2, f2, s2, d2, k2 = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
    n3, f3, s3, d3, k3 = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0

    print(findCheapestPrice(n1, f1, s1, d1, k1))
    print(findCheapestPrice(n2, f2, s2, d2, k2))
    print(findCheapestPrice(n3, f3, s3, d3, k3))
