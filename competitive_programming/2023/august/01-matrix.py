'''
Created Date: 2023-08-17
Qn: Given an m x n binary matrix mat, return the distance of the nearest 0 for
    each cell.

    The distance between two adjacent cells is 1.
Link: https://leetcode.com/problems/01-matrix/
Notes:
    - use bfs
'''
from collections import deque

def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    M, N = len(mat), len(mat[0])
    res = [[-1] * N for _ in range(M)]

    # mark zero
    q = deque()
    for r in range(M):
        for c in range(N):
            if mat[r][c] == 0:
                res[r][c] = 0
                q.append((r, c))

    # mark neighbours
    dirs = [0, 1, 0, -1, 0]
    while q:
        r, c = q.popleft()
        cur_val = res[r][c]
        for i in range(len(dirs)-1):
            nr, nc = r + dirs[i], c + dirs[i+1]
            if 0 <= nr < M and 0 <= nc < N and res[nr][nc] == -1:
                res[nr][nc] = cur_val + 1
                q.append((nr, nc))
    return res

    # bfs approach
    # M, N = len(mat), len(mat[0])
    # def bfs(r: int, c: int) -> int:
    #     if mat[r][c] == 0: return 0
    #     q = deque([(r, c)])
    #     dirs = [0, 1, 0, -1, 0]
    #     dist = 0
    #     while q:
    #         for _ in range(len(q)):
    #             r, c = q.popleft()
    #             for i in range(len(dirs)-1):
    #                 nr, nc = r + dirs[i], c + dirs[i+1]
    #                 if 0 <= nr < M and 0 <= nc < N:
    #                     if mat[nr][nc] == 0:
    #                         return dist + 1
    #                     else:
    #                         q.append((nr, nc))
    #         dist += 1
    #     return -1
    #
    # return [[bfs(r, c) for c in range(N)] for r in range(M)]

if __name__ == '__main__':
    m1 = [[0,0,0],[0,1,0],[0,0,0]]
    m2 = [[0,0,0],[0,1,0],[1,1,1]]

    print(updateMatrix(m1))
    print(updateMatrix(m2))
