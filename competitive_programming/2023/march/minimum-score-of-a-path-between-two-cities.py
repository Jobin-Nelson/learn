'''
Created Date: 2023-03-22
Qn: You are given a positive integer n representing n cities numbered from 1 to
    n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei]
    indicates that there is a bidirectional road between cities ai and bi with
    a distance equal to distancei. The cities graph is not necessarily
    connected.

    The score of a path between two cities is defined as the minimum distance
    of a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note:

        - A path is a sequence of roads between two cities. 
        - It is allowed for a path to contain the same road multiple times, and
          you can visit cities 1 and n multiple times along the path. 
        - The test cases are generated such that there is at least one path
          between 1 and n.
Link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
Notes:
    - use dfs
    - find the smallest distance out of all the path connecting 1 to n
'''
from collections import defaultdict

def minScore(n: int, roads: list[list[int]]) -> int:
    adj = defaultdict(list)

    for src, dst, dist in roads:
        adj[src].append((dst, dist))
        adj[dst].append((src, dist))

    def dfs(i: int) -> None:
        if i in visited: return
        nonlocal res

        visited.add(i)
        for nei, dist in adj[i]:
            res = min(res, dist)
            dfs(nei)

    res = float('inf')
    visited = set()
    dfs(1)
    return res

if __name__ == '__main__':
    n1, r1 = 4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    n2, r2 = 4, [[1,2,2],[1,3,4],[3,4,7]]

    print(minScore(n1, r1))
    print(minScore(n2, r2))
