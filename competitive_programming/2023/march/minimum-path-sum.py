'''
Created Date: 2023-03-27
Qn: Given a m x n grid filled with non-negative numbers, find a path from top
    left to bottom right, which minimizes the sum of all numbers along its
    path.

    Note: You can only move either down or right at any point in time.
Link: https://leetcode.com/problems/minimum-path-sum/
Notes:
    - use dp
    - find minPathSum for each node
'''
def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Finding the minPathSum for first row
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]

    # Finding the minPathSum for first column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]

if __name__ == '__main__':
    g1 = [[1,3,1],[1,5,1],[4,2,1]]
    g2 = [[1,2,3],[4,5,6]]

    print(minPathSum(g1))
    print(minPathSum(g2))
