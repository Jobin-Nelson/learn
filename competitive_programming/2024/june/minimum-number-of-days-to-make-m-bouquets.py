"""
Created Date: 2024-06-19
Qn: You are given an integer array bloomDay, an integer m and an integer k.

    You want to make m bouquets. To make a bouquet, you need to use k adjacent
    flowers from the garden.

    The garden consists of n flowers, the ith flower will bloom in the
    bloomDay[i] and then can be used in exactly one bouquet.

    Return the minimum number of days you need to wait to be able to make m
    bouquets from the garden. If it is impossible to make m bouquets return -1.
Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Notes:
    - use binary search
"""
def minDays(bloomDay: list[int], m: int, k: int) -> int:
    n = len(bloomDay)
    if m * k > n: return -1
    
    def can_create_bouquets(bloom_days: list[int], days: int) -> bool:
        bouquets = 0
        flowers = 0
        for f in bloom_days:
            if f - days <= 0:
                flowers += 1
            else:
                flowers = 0
            if flowers == k:
                bouquets += 1
                if bouquets == m:
                    return True
                flowers = 0
        return False

    l, r = 0, max(bloomDay)
    while l <= r:
        days = l + ((r-l)>>1)
        if can_create_bouquets(bloomDay, days):
            r = days - 1
        else:
            l = days + 1
    return l

if __name__ == '__main__':
    b1, m1, k1 = [1,10,3,10,2], 3, 1
    b2, m2, k2 = [1,10,3,10,2], 3, 2
    b3, m3, k3 = [7,7,7,7,12,7,7], 2, 3
    b4, m4, k4 = [1,2,4,9,3,4], 2, 2

    print(minDays(b1, m1, k1))
    print(minDays(b2, m2, k2))
    print(minDays(b3, m3, k3))
    print(minDays(b4, m4, k4))
