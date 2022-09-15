'''
Created Date: 2022-09-10
Qn: You are given an integer array prices where prices[i] is the price of a
    given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k
    transactions.

    You may not engage in multiple transactions simultaneously (i.e., you must sell
    the stock before you buy again).
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Notes:
    - iterate k times tracking pos and profit 
'''
def maxProfit(k: int, prices: list[int]) -> int:
    if not prices: return 0
    N = len(prices)
    dp = [0] * N

    if k > N:
        B = [prices[i] - prices[i-1] for i in range(1, N)]
        return sum(b for b in B if b > 0)

    for _ in range(k):
        pos = -prices[0]
        profit = 0

        for i in range(1, N):
            pos = max(pos, dp[i] - prices[i])
            profit = max(profit, pos + prices[i])
            dp[i] = profit
    return dp[-1]

if __name__ == '__main__':
    p1, k1 = [2, 4, 1], 2
    p2, k2 = [3, 2, 6, 5, 0, 3], 2

    print(maxProfit(k1, p1))
    print(maxProfit(k2, p2))
