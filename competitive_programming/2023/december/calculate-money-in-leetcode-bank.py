"""
Created Date: 2023-12-06
Qn: Hercy wants to save money for his first car. He puts money in the Leetcode
    bank every day.

    He starts by putting in $1 on Monday, the first day. Every day from Tuesday
    to Sunday, he will put in $1 more than the day before. On every subsequent
    Monday, he will put in $1 more than the previous Monday.

    Given n, return the total amount of money he will have in the Leetcode bank
    at the end of the nth day.
Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
Notes:
    - use math formulae (f + l) * len / 2
"""
def totalMoney(n: int) -> int:
    weeks, rem = divmod(n, 7)
    first = 28
    last = first + 7 * (weeks-1)
    res = ((first + last) * weeks) >> 1

    monday = weeks + 1
    for i in range(rem):
        res += i + monday
    return res
    # res = 0
    # monday = 1
    # while n > 0:
    #     for day in range(min(n, 7)):
    #         res += monday + day
    #     n -= 7
    #     monday += 1
    # return res

if __name__ == '__main__':
    n1 = 4
    n2 = 10
    n3 = 20

    print(totalMoney(n1))
    print(totalMoney(n2))
    print(totalMoney(n3))
