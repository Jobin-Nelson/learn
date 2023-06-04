'''
Created Date: 2023-06-01
Qn: Given an n x n binary matrix grid, return the length of the shortest clear
    path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
    0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

        - All the visited cells of the path are 0.
        - All the adjacent cells of the path are 8-directionally connected
          (i.e., they are different and they share an edge or a corner).

    The length of a clear path is the number of visited cells of this path.
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Notes:
    - use bfs or dfs
'''
from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    N = len(grid)
    if grid[0][0] or grid[N-1][N-1]: return -1

    grid[0][0] = 1
    res, q = 1, deque([(0, 0)])
    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (N-1, N-1): return res

            for x, y in dirs:
                dx, dy = i + x, j + y
                if 0 <= dx < N and 0 <= dy < N and grid[dx][dy] == 0:
                    grid[dx][dy] = 1 # mark as visited
                    q.append((dx, dy))

        res += 1
    return -1

# def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
#     if grid[0][0] == 1: return -1
#     N = len(grid)
#     dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#     visited = set()
#     dp = {}
#
#     def dfs(i: int, j: int) -> int | float:
#         if (i, j) == (N-1, N-1): return 1
#         if (i, j) in visited: return float('inf')
#         if (i, j) in dp: return dp[(i, j)]
#
#         visited.add((i, j))
#         res = float('inf')
#         for x, y in dirs:
#             dx, dy = i + x, j + y
#             if 0 <= dx < N and 0 <= dy < N and grid[dx][dy] == 0 and (dx, dy) not in visited:
#                 res = min(res, 1 + dfs(dx, dy))
#         dp[(i, j)] = res
#         return res
#     short_path = dfs(0, 0)
#     return -1 if short_path == float('inf') else short_path

if __name__ == '__main__':
    g1 = [[0,1],[1,0]]
    g2 = [[0,0,0],[1,1,0],[1,1,0]]
    g3 = [[1,0,0],[1,1,0],[1,1,0]]

    print(shortestPathBinaryMatrix(g1))
    print(shortestPathBinaryMatrix(g2))
    print(shortestPathBinaryMatrix(g3))
