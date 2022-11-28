'''
Created Date: 13-06-2022
Qn: Given a triangle array, return the minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below. 
    More formally, if you are on index i on the current row, you may move 
    to either index i or index i + 1 on the next row.
Link: https://leetcode.com/problems/triangle/
Notes:
    - Can use recursion or Iteration
    - Bottom up approach
'''
def minimumTotal(triangle: list[list[int]]) -> int:
    # Recursion method
    # memo = {}
    # def dfs(r, c):
    #     if (r, c) in memo:
    #         return memo[(r, c)]
    #     if r == len(triangle) or c == len(triangle[r]):
    #         return 0
    #
    #     memo[(r, c)] = triangle[r][c] + min(dfs(r+1, c), dfs(r+1, c+1))
    #     return memo[(r, c)]
    # return dfs(0, 0)
    
    # Iteration method
    N = len(triangle)
    for r in range(N-2, -1, -1):
        for c in range(r+1):
            triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
    return triangle[0][0]

if __name__ == '__main__':
    t1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    t2 = [[-10]]
    print(minimumTotal(t1))
    print(minimumTotal(t2))
