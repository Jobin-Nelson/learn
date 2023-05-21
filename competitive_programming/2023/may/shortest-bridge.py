'''
Created Date: 2023-05-21
Qn: You are given an n x n binary matrix grid where 1 represents land and 0
    represents water.

    An island is a 4-directionally connected group of 1's not connected to any
    other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.
Link: https://leetcode.com/problems/shortest-bridge/
Notes:
    - use dfs to find all cells of one island and store it in hashset
    - convert the set to queue and use bfs to find the next island
    - no need to for djikshtra's algo since the graph is not weighted
'''
from collections import deque

def shortestBridge(grid: list[list[int]]) -> int:
    dirs = [1, 0, -1, 0, 1] # (1, 0), (0, -1), (-1, 0), (0, 1)
    R, C = len(grid), len(grid[0])
    visited = set()
    def invalid(r: int, c: int) -> bool:
        return r < 0 or r == R or c < 0 or c == C

    def dfs(r: int, c: int) -> None:
        if invalid(r, c) or not grid[r][c] or (r, c) in visited: return
        visited.add((r, c))
        for i in range(1, len(dirs)):
            dfs(r + dirs[i-1], c + dirs[i])

    def bfs() -> int | None:
        res, q = 0, deque(visited)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(1, len(dirs)):
                    dr, dc = r + dirs[i-1], c + dirs[i]
                    if invalid(dr, dc) or (dr, dc) in visited: continue
                    if grid[dr][dc]: return res
                    q.append((dr, dc))
                    visited.add((dr, dc))
            res += 1

    for r in range(R):
        for c in range(C):
            if grid[r][c]:
                dfs(r, c)
                return bfs()


if __name__ == '__main__':
    g1 = [[0,1],[1,0]]
    g2 = [[0,1,0],[0,0,0],[0,0,1]]
    g3 = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

    print(shortestBridge(g1))
    print(shortestBridge(g2))
    print(shortestBridge(g3))
