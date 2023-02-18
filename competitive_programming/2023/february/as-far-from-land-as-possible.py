'''
Created Date: 2023-02-10
Qn: Given an n x n grid containing only values 0 and 1, where 0 represents
    water and 1 represents land, find a water cell such that its distance to
    the nearest land cell is maximized, and return the distance. If no land or
    water exists in the grid, return -1.

    The distance used in this problem is the Manhattan distance: the distance
    between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
Link: https://leetcode.com/problems/as-far-from-land-as-possible/
Notes:
    - use bfs
    - increment as you iterate over water
    - return the maximum iteration
'''
from collections import deque

def maxDistance(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    dirs = [0, 1, 0, -1, 0]
    q = deque()
    water = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                water += 1
            else:
                q.append((i, j))

    if water == 0 or water == m * n: return -1

    res = d = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            res = d

            for k in range(4):
                x = i + dirs[k]
                y = j + dirs[k+1]

                if x < 0 or x == m or y < 0 or y == n: continue
                if grid[x][y] > 0: continue

                q.append((x, y))
                grid[x][y] = 2
        d += 1

    return res

if __name__ == '__main__':
    g1 = [[1,0,1],[0,0,0],[1,0,1]]
    g2 = [[1,0,0],[0,0,0],[0,0,0]]

    print(maxDistance(g1))
    print(maxDistance(g2))
