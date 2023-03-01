'''
Created Date: 2023-02-25
Qn: You are given an array prices where prices[i] is the price of a given stock
    on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you
    cannot achieve any profit, return 0.
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Notes:
    - use two pointer
    - if profit is less than zero move the left pointer to right pointer
'''
def maxProfit(prices: list[int]) -> int:
    max_profit = l = 0

    for r in range(1, len(prices)):
        profit = prices[r] - prices[l]
        if profit < 0:
            l = r
        else:
            max_profit = max(max_profit, profit)

    return max_profit

if __name__ == '__main__':
    p1 = [7,1,5,3,6,4]
    p2 = [7,6,4,3,1]
    
    print(maxProfit(p1))
    print(maxProfit(p2))
