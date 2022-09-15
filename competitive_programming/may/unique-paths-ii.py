'''
Qn: An obstacle and space are marked as 1 or 0 respectively in grid. 
    A path that the robot takes cannot include any square that is an obstacle.
    Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
Link: https://leetcode.com/problems/unique-paths-ii/
Notes:
    - mark every first row and col that is not blocked as one
    - iteratively count the sum of previous row and col 
    - return the value of the last cell
'''
def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    R, C = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        if obstacleGrid[r][0] == 1: break
        dp[r][0] = 1
    for c in range(C):
        if obstacleGrid[0][c] == 1: break
        dp[0][c] = 1

    for r in range(1, R):
        for c in range(1, C):
            if obstacleGrid[r][c] == 1: continue
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[-1][-1]

if __name__ == '__main__':
    g1 = [[0,0,0],[0,1,0],[0,0,0]]
    g2 = [[0,1],[0,0]]
    print(uniquePathsWithObstacles(g1))
    print(uniquePathsWithObstacles(g2))
