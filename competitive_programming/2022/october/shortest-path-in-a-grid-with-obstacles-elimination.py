'''
Created Date: 2022-10-30
Qn: You are given an m x n integer matrix grid where each cell is either 0
    (empty) or 1 (obstacle). You can move up, down, left, or right from and to
    an empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner 
    (0, 0) to the lower right corner (m - 1, n - 1) given that you can
    eliminate at most k obstacles. If it is not possible to find such walk
    return -1.
Link: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
Notes:
    - bfs
    - x, y, obstacle_left, steps
'''
from collections import deque

def shortestPath(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    q = deque([(0, 0, k, 0)]) # x, y, obstacle_left, steps

    while q:
        x, y, left, steps = q.popleft()
        if (x, y, left) in visited or left < 0: continue
        if (x, y) == (m-1, n-1): return steps
        visited.add((x, y, left))
        if grid[x][y] == 1: left -= 1

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x, new_y = x + dx, y + dy
            if 0<=new_x<m and 0<=new_y<n:
                q.append((new_x, new_y, left, steps+1))
    return -1

if __name__ == '__main__':
    g1, k1 = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1
    g2, k2 = [[0,1,1],[1,1,1],[1,0,0]], 1

    print(shortestPath(g1, k1))
    print(shortestPath(g2, k2))
