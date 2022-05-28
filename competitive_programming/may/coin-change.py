'''
Qn: You are given an integer array coins representing coins of different 
    denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
Link: https://leetcode.com/problems/coin-change/
Notes:
- dynamic programming qn find sum of coins from 0->amount by caching previous values
'''
def coinChange(coins: list[int], amount: int) -> int:
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for a in range(amount+1):
        for c in coins:
            if a+c <= amount and dp[a] != amount+1:
                dp[a+c] = min(dp[a+c], 1 + dp[a])
    return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == '__main__':
    c1, a1 = [1, 2, 5], 11
    c2, a2 = [2], 3
    c3, a3 = [1], 0
    print(coinChange(c1, a1))
    print(coinChange(c2, a2))
    print(coinChange(c3, a3))
