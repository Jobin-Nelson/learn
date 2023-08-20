'''
Created Date: 2023-08-18
Qn: There is an infrastructure of n cities with some number of roads connecting
    these cities. Each roads[i] = [ai, bi] indicates that there is a
    bidirectional road between cities ai and bi.

    The network rank of two different cities is defined as the total number of
    directly connected roads to either city. If a road is directly connected to
    both cities, it is only counted once.

    The maximal network rank of the infrastructure is the maximum network rank
    of all pairs of different cities.

    Given the integer n and the array roads, return the maximal network rank of
    the entire infrastructure.
Link: https://leetcode.com/problems/maximal-network-rank/
Notes:
    - use hashmap to store hashset of adjacent nodes
    - current_rank = indegree - common connected nodes
    - return max of current_rank
'''
from collections import defaultdict

def maximalNetworkRank(n: int, roads: list[list[int]]) -> int:
    res = 0
    adj = defaultdict(set)

    for a, b in roads:
        adj[a].add(b)
        adj[b].add(a)

    for n1 in range(n):
        for n2 in range(n1+1, n):
            current_rank = len(adj[n1]) + len(adj[n2])
            if n2 in adj[n1]: current_rank -= 1
            res = max(res, current_rank)
    return res

if __name__ == '__main__':
    n1, r1 = 4, [[0,1],[0,3],[1,2],[1,3]]
    n2, r2 = 5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    n3, r3 = 8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

    print(maximalNetworkRank(n1, r1))
    print(maximalNetworkRank(n2, r2))
    print(maximalNetworkRank(n3, r3))
