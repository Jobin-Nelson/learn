"""
Created Date: 2024-02-08
Qn: Given an integer n, return the least number of perfect square numbers that
    sum to n.

    A perfect square is an integer that is the square of an integer; in other
    words, it is the product of some integer with itself. For example, 1, 4, 9,
    and 16 are perfect squares while 3 and 11 are not.

Link: https://leetcode.com/problems/perfect-squares/
Notes:
    - use dp
"""
def numSquares(n: int) -> int:
    dp = [n] * (n+1)
    dp[0] = 0
    
    for target in range(1, n+1):
        for s in range(1, target+1):
            square = s * s
            if target - square < 0: break
            dp[target] = min(dp[target], dp[target-square] + 1)
    return dp[n]

if __name__ == '__main__':
    n1 = 12
    n2 = 13

    print(numSquares(n1))
    print(numSquares(n2))
