'''
Created Date: 2022-11-09
Qn: Design an algorithm that collects daily price quotes for some stock and
    returns the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of
    consecutive days (starting from today and going backward) for which the
    stock price was less than or equal to today's price.

    - For example, if the price of a stock over the next 7 days were
      [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].

    Implement the StockSpanner class:

        - StockSpanner() Initializes the object of the class. 
        - int next(int price) Returns the span of the stock's price given that
          today's price is price.
Link: https://leetcode.com/problems/online-stock-span/
Notes:
    - use stack 
    - we only need to track previous price and previous span
'''
class StockSpanner():
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res

if __name__ == '__main__':
    s1 = StockSpanner()
    p1 = [100, 80, 60, 70, 60, 75, 85]
    for p in p1:
        print(s1.next(p))

