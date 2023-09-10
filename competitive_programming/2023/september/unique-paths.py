'''
Created Date: 2023-09-03
Qn: There is a robot on an m x n grid. The robot is initially located at the
    top-left corner (i.e., grid[0][0]). The robot tries to move to the
    bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
    either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths
    that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal
    to 2 * 109.
Link: https://leetcode.com/problems/unique-paths/
Notes:
    - use dp
'''
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n
    for i in range(1, m):
        ndp = [1] * n
        for j in range(1, n):
            ndp[j] = dp[j] + ndp[j-1]
        dp = ndp
    return dp[-1]

if __name__ == '__main__':
    m1, n1 = 3, 7
    m2, n2 = 3, 2

    print(uniquePaths(m1, n1))
    print(uniquePaths(m2, n2))
