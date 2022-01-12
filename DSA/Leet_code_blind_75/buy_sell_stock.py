# One pointer
class Solution:
    def buy_sell(self, prices: List[int])->int:
        buy = prices[0]
        max_profit = 0

        for num in prices:
            profit = num - buy
            max_profit = profit if profit>max_profit else max_profit
            buy = num if buy>num else buy
        return max_profit

# Two pointer
class Solution_2:
    def max_profit(self, prices: List[int])->int:
        b,s = 0,1 # b=buy, s=sell
        max_p = 0
        while s<len(prices):
            if prices[b]<prices[s]:
                profit = prices[s]-prices[b]
                max_p = max(profit, max_p)
            else:
                b=s
            s+=1
        return max_p
