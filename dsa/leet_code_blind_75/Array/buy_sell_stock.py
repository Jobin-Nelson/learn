'''
Qn: You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock
Return the maximum profit you can achieve from this transaction. If you cannot achieve profit return 0
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Notes: One pointer, keep track of the minimum value and maximum profit at each iteration
'''

from itertools import accumulate
from operator import sub


# One pointer
def buy_sell(prices: list[int]) -> int:
    # Functional approach
    return max(map(sub, prices, accumulate(prices, min, initial=prices[0])))

    # Imperative approach
    # buy = prices[0]
    # profit = 0
    #
    # for num in prices:
    #     buy = min(buy, num)
    #     profit = max(profit, num - buy)
    # return profit


# Two pointer
def max_profit(prices: list[int]) -> int:
    b, s = 0, 1  # b=buy, s=sell
    max_p = 0
    while s < len(prices):
        if prices[b] < prices[s]:
            profit = prices[s] - prices[b]
            max_p = max(profit, max_p)
        else:
            b = s
        s += 1
    return max_p


if __name__ == '__main__':
    num1 = [7, 1, 5, 3, 6, 4]
    num2 = [7, 6, 4, 3, 1]
    print(buy_sell(num1))
    print(buy_sell(num2))
