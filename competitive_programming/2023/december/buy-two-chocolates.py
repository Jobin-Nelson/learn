"""
Created Date: 2023-12-20
Qn: You are given an integer array prices representing the prices of various
    chocolates in a store. You are also given a single integer money, which
    represents your initial amount of money.

    You must buy exactly two chocolates in such a way that you still have some
    non-negative leftover money. You would like to minimize the sum of the
    prices of the two chocolates you buy.

    Return the amount of money you will have leftover after buying the two
    chocolates. If there is no way for you to buy two chocolates without ending
    up in debt, return money. Note that the leftover must be non-negative.
Link: https://leetcode.com/problems/buy-two-chocolates/
Notes:
"""
def buyChoco(prices: list[int], money: int) -> int:
    m1, m2 = min(prices[0], prices[1]), max(prices[0], prices[1])
    for p in prices[2:]:
        if p < m1:
            m2 = m1
            m1 = p
        elif p < m2:
            m2 = p
    leftover = money - (m1 + m2)
    return money if leftover < 0 else leftover
    # leftover = money - sum(sorted(prices)[:2])
    # return money if (leftover < 0) else leftover


if __name__ == '__main__':
    p1, m1 = [1, 2, 2], 3
    p2, m2 = [3, 2, 3], 3

    print(buyChoco(p1, m1))
    print(buyChoco(p2, m2))
