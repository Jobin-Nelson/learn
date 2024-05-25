"""
Created Date: 2024-05-15
Qn: You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

        - A cell containing a thief if grid[r][c] = 1 
        - An empty cell if grid[r][c] = 0

    You are initially positioned at cell (0, 0). In one move, you can move to
    any adjacent cell in the grid, including cells containing thieves.

    The safeness factor of a path on the grid is defined as the minimum
    manhattan distance from any cell in the path to any thief in the grid.

    Return the maximum safeness factor of all paths leading to cell (n - 1, n -
    1).

    An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c -
    1), (r + 1, c) and (r - 1, c) if it exists.

    The Manhattan distance between two cells (a, b) and (x, y) is equal to |a -
    x| + |b - y|, where |val| denotes the absolute value of val
Link: https://leetcode.com/problems/find-the-safest-path-in-a-grid/
Notes:
    - precompute the min dist to the thief for the entire grid
    - use modified dijkstra's algorithm to find path
"""
from collections import deque
import heapq

def maximumSafenessFactor(grid: list[list[int]]) -> int:
    if grid[0][0] == 1: return 0
    R, C = len(grid), len(grid[0])

    def in_bound(r: int, c: int) -> bool:
        return 0 <= r < R and 0 <= c < C

    def precompute(min_dist: list[list[int]]):
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    min_dist[r][c] = 0
        while q:
            r, c, dist = q.popleft()
            neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
            for dr, dc in neighbors:
                if in_bound(dr, dc) and min_dist[dr][dc] == -1:
                    min_dist[dr][dc] = dist + 1
                    q.append((dr, dc, dist+1))

    min_dist = [[-1]*C for _ in range(R)]
    precompute(min_dist)

    h = [(-min_dist[0][0],0,0)]
    visited = set([(0,0)])
    while h:
        dist, r, c = heapq.heappop(h)
        dist = -dist
        if (r,c) == (R-1,C-1):
            return dist
        neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        for dr, dc in neighbors:
            if in_bound(dr,dc) and (dr,dc) not in visited:
                visited.add((dr,dc))
                nei_dist = min(dist, min_dist[dr][dc])
                heapq.heappush(h, (-nei_dist, dr, dc))
    return -1

if __name__ == '__main__':
    g1 = [[1,0,0],[0,0,0],[0,0,1]]
    g2 = [[0,0,1],[0,0,0],[0,0,0]]
    g3 = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]

    print(maximumSafenessFactor(g1))
    print(maximumSafenessFactor(g2))
    print(maximumSafenessFactor(g3))
