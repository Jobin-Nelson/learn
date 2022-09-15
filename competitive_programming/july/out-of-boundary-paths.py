'''
Created Date: 16-07-2022
Qn: There is an m x n grid with a ball. The ball is initially at the position
    [startRow, startColumn]. You are allowed to move the ball to one of the four
    adjacent cells in the grid (possibly out of the grid crossing the grid
    boundary). You can apply at most maxMove moves to the ball. 

    Given the five integers m, n, maxMove, startRow, startColumn, return the 
    number of paths to move the ball out of the grid boundary. Since the answer
    can be very large, return it modulo 10^9 + 7.
Link: https://leetcode.com/problems/out-of-boundary-paths/
Notes:
    - Recursion and memoization
'''
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    memo = {}
    def dfs(r, c, M):
        if (r, c, M) in memo: return memo[(r, c, M)]
        if r<0 or c<0 or r>=m or c>=n: return 1
        if M==0: return 0
        count = 0
        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
            count += dfs(r+x, c+y, M-1)
        memo[(r, c, M)] = count
        return count
    return dfs(startRow, startColumn, maxMove) % (10**9+7)


if __name__ == '__main__':
    m1, n1, mm1, sr1, sc1 = 2, 2, 2, 0, 0
    m2, n2, mm2, sr2, sc2 = 1, 3, 3, 0, 1

    print(findPaths(m1, n1, mm1, sr1, sc1))
    print(findPaths(m2, n2, mm2, sr2, sc2))
