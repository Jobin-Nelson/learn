'''
Qn: Given an n x n binary matrix grid, 
    return the length of the shortest clear path in the matrix. 
    If there is no clear path, return -1.
    A clear path in a binary matrix is a path from the top-left cell 
    (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
        - All the visited cells of the path are 0.
        - All the adjacent cells of the path are 8-directionally connected 
        (i.e., they are different and they share an edge or a corner)
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Notes:
- use bfs to find the shortest path
'''
from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    R = C = len(grid)
    visited = set()
    q = deque()
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1))

    if grid[0][0] == 0:
        q.append((1, (0, 0)))
        visited.add((0, 0))

    while q:
        steps, row_col = q.popleft()
        r, c = row_col
        if (r, c) == (R-1, C-1):
            return steps
        for i, j in dirs:
            new_r, new_c = r + i, c + j
            if 0<=new_r<R and 0<=new_c<C and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                q.append((steps+1, (new_r, new_c)))
                visited.add((new_r, new_c))
    return -1


if __name__ == '__main__':
    g1 = [[0, 1], [1, 0]]
    g2 = [[0,0,0],[1,1,0],[1,1,0]]
    g3 = [[1,0,0],[1,1,0],[1,1,0]]

    print(shortestPathBinaryMatrix(g1))
    print(shortestPathBinaryMatrix(g2))
    print(shortestPathBinaryMatrix(g3))

