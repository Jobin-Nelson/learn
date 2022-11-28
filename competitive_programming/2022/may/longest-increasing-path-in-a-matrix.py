'''
Qn: Given m x n integeres matrix, return the length of the longest increasing path in matrix
    From each cell, you can either move in four directions: left, right, up, or down. 
    You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Notes:
    - dfs with caching 
'''
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    R, C = len(matrix), len(matrix[0])
    dp = {}
    def dfs(r, c, prev):
        row_outbound = r < 0 or r >= R
        col_outbound = c < 0 or c >= C
        if row_outbound or col_outbound or matrix[r][c] <= prev:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]
        res = 1
        res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
        dp[(r, c)] = res
        return res
    LIP = 0
    for r in range(R):
        for c in range(C):
            LIP = max(LIP, dfs(r, c, -1))
    return LIP

if __name__ == '__main__':
    m1 = [[9,9,4],[6,6,8],[2,1,1]]
    m2 = [[3,4,5],[3,2,6],[2,2,1]]
    m3 = [[1]]
    print(longestIncreasingPath(m1))
    print(longestIncreasingPath(m2))
    print(longestIncreasingPath(m3))
