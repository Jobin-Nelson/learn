'''
Created Date: 2023-09-10
Qn: Given n orders, each order consist in pickup and delivery services. 

    Count all valid pickup/delivery possible sequences such that delivery(i) is
    always after of pickup(i). 

    Since the answer may be too large, return it modulo 10^9 + 7.
Link: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
Notes:
    - use permutation and divide by half to account for the condition that
      pickup should happen before delivery
'''
def countOrders(n: int) -> int:
    res, slots = 1, 2 * n

    while slots > 0:
        res *= slots * (slots - 1) // 2
        slots -= 2

    return res % (10**9 + 7)

if __name__ == '__main__':
    n1 = 1
    n2 = 2
    n3 = 3

    print(countOrders(n1))
    print(countOrders(n2))
    print(countOrders(n3))
