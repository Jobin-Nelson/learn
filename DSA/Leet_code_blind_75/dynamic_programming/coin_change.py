'''
Qn:You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Link: https://leetcode.com/problems/coin-change/
Notes:
- break the problem into subproblems and work from bottom 0 -> amount where each answer is the min number of coins to reach the remainder(amount-coin) + 1
'''
# Bottom-up
def coin_change(self, coins: list[int], amount: int) -> int:
    dp = [amount+1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])

    return dp[amount] if dp[amount] != (amount+1) else -1

if __name__ == '__main__':
    c1, c2, c3 = [1, 2, 5], [2], [1]
    a1, a2, a3 = 11, 3, 0
    print(coin_change(c1, a1))
    print(coin_change(c2, a2))
    print(coin_change(c3, a3))