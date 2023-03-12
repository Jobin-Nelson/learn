'''
Created Date: 2023-03-08
Qn: Koko loves to eat bananas. There are n piles of bananas, the ith pile has
    piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she
    chooses some pile of bananas and eats k bananas from that pile. If the pile
    has less than k bananas, she eats all of them instead and will not eat any
    more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas
    before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h
    hours.
Link: https://leetcode.com/problems/koko-eating-bananas/
Notes:
    - use binary search
    - lowest speed is 1 max speed is max(piles)
    - binary search to find the first speed that has time <= h
'''
import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)

    while l < r:
        m = l + ((r - l) >> 1)
        if sum(math.ceil(p / m) for p in piles) <= h:
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    p1, h1 = [3,6,7,11], 8
    p2, h2 = [30,11,23,4,20], 5
    p3, h3 = [30,11,23,4,20], 6

    print(minEatingSpeed(p1, h1))
    print(minEatingSpeed(p2, h2))
    print(minEatingSpeed(p3, h3))
