"""
Created Date: 2024-01-26
Qn: There is an m x n grid with a ball. The ball is initially at the position
    [startRow, startColumn]. You are allowed to move the ball to one of the
    four adjacent cells in the grid (possibly out of the grid crossing the grid
    boundary). You can apply at most maxMove moves to the ball.

    Given the five integers m, n, maxMove, startRow, startColumn, return the
    number of paths to move the ball out of the grid boundary. Since the answer
    can be very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/out-of-boundary-paths/
Notes:
    - use bottom up iterative or memoized recursive approach
"""
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    # dfs approach
    # mod = 10**9+7
    # @cache
    # def dfs(r: int, c: int, m: int) -> int:
    #     if not (0 <= r < m or  0 <= c < n): return 1
    #     if m == 0: return 0
    #     return (
    #         dfs(r+1, c, m-1) +
    #         dfs(r-1, c, m-1) +
    #         dfs(r, c+1, m-1) +
    #         dfs(r, c-1, m-1)
    #     ) % mod
    # return dfs(startRow, startColumn, maxMove) % mod


    # bottom up iterative approach
    prev = [[0] * n for _ in range(m)]
    dirs = [0, 1, 0, -1, 0]
    mod = 10**9+7
    for _ in range(maxMove):
        cur = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for i in range(len(dirs)-1):
                    dr, dc = r + dirs[i], c + dirs[i+1]
                    if 0 <= dr < m and 0 <= dc < n:
                        cur[r][c] = (cur[r][c] + prev[dr][dc]) % mod
                    else:
                        cur[r][c] += 1
        prev = cur
    return prev[startRow][startColumn]

if __name__ == '__main__':
    m1, n1, mm1, sr1, sc1 = 2, 2, 2, 0, 0
    m2, n2, mm2, sr2, sc2 = 1, 3, 3, 0, 1
    m3, n3, mm3, sr3, sc3 = 8, 7, 16, 1, 5

    print(findPaths(m1, n1, mm1, sr1, sc1))
    print(findPaths(m2, n2, mm2, sr2, sc2))
    print(findPaths(m3, n3, mm3, sr3, sc3))
