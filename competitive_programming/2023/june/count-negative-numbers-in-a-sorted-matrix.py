'''
Created Date: 2023-06-08
Qn: Given a m x n matrix grid which is sorted in non-increasing order both
    row-wise and column-wise, return the number of negative numbers in grid.
Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Notes:
    - since it is sorted we can use binary search to find the beginning of the
      negative numbers
    - linear traversal is also an alternative
'''
def countNegatives(grid: list[list[int]]) -> int:
    M, N = len(grid), len(grid[0])
    res = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] < 0:
                res += (N - j)
                break
    return res

if __name__ == '__main__':
    g1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    g2 = [[3,2],[1,0]]

    print(countNegatives(g1))
    print(countNegatives(g2))
