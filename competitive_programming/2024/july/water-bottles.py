"""
Created Date: 2024-07-07
Qn: There are numBottles water bottles that are initially full of water. You
    can exchange numExchange empty water bottles from the market with one full
    water bottle.

    The operation of drinking a full water bottle turns it into an empty
    bottle.

    Given the two integers numBottles and numExchange, return the maximum
    number of water bottles you can drink.
Link: https://leetcode.com/problems/water-bottles/
Notes:
    - use simulation
"""
def numWaterBottles(numBottles: int, numExchange: int) -> int:
    res = 0
    while numBottles >= numExchange:
        k = numBottles // numExchange
        res += numExchange * k
        numBottles -= numExchange * k
        numBottles += k
    return res + numBottles

if __name__ == '__main__':
    nb1, ne1 = 9, 3
    nb2, ne2 = 15, 4

    print(numWaterBottles(nb1, ne1))
    print(numWaterBottles(nb2, ne2))
