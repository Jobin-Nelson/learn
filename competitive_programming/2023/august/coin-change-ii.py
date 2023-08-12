'''
Created Date: 2023-08-11
Qn: You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount
    of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.
Link: https://leetcode.com/problems/coin-change-ii/
Notes:
    - use dp
'''
def change(amount: int, coins: list[int]) -> int:
    N = len(coins)
    dp = [[0] * (amount+1) for _ in range(N+1)]

    for i in range(N):
        dp[i][0] = 1

    for i in range(N-1, -1, -1):
        for j in range(1, amount+1):
            if coins[i] > j:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i][j-coins[i]] + dp[i+1][j]

    return dp[0][amount]

if __name__ == '__main__':
    a1, c1 = 5, [1,2,5]
    a2, c2 = 3, [2]
    a3, c3 = 10, [10]

    print(change(a1, c1))
    print(change(a2, c2))
    print(change(a3, c3))
