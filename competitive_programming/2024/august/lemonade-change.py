"""
Created Date: 2024-08-15
Qn: At a lemonade stand, each lemonade costs $5. Customers are standing in a
    queue to buy from you and order one at a time (in the order specified by
    bills). Each customer will only buy one lemonade and pay with either a $5,
    $10, or $20 bill. You must provide the correct change to each customer so
    that the net transaction is that the customer pays $5.

    Note that you do not have any change in hand at first.

    Given an integer array bills where bills[i] is the bill the ith customer
    pays, return true if you can provide every customer with the correct
    change, or false otherwise.
Link: https://leetcode.com/problems/lemonade-change/
Notes:
    - use variables to keep count
"""


def lemonadeChange(bills: list[int]) -> bool:
    fives, tens = 0, 0

    for n in bills:
        if n == 5:
            fives += 1
        elif n == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True


if __name__ == '__main__':
    b1 = [5, 5, 5, 10, 20]
    b2 = [5, 5, 10, 10, 20]

    print(lemonadeChange(b1))
    print(lemonadeChange(b2))
