'''
Created Date: 2023-06-22
Qn: You are given an array prices where prices[i] is the price of a given stock
    on the ith day, and an integer fee representing a transaction fee.

    Find the maximum profit you can achieve. You may complete as many
    transactions as you like, but you need to pay the transaction fee for each
    transaction.

    Note: You may not engage in multiple transactions simultaneously (i.e., you
    must sell the stock before you buy again).
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Notes:
    - use two variables hold and free
'''
def maxProfit(prices: list[int], fee: int) -> int:
    N = len(prices)
    hold, free = -prices[0], 0

    for i in range(1, N):
        hold, free = max(hold, free - prices[i]), max(free, hold + prices[i] - fee)
    return free

if __name__ == '__main__':
    p1, f1 = [1,3,2,8,4,9], 2
    p2, f2 = [1,3,7,5,10,3], 3

    print(maxProfit(p1, f1))
    print(maxProfit(p2, f2))
