'''
Created Date: 2023-02-22
Qn: A conveyor belt has packages that must be shipped from one port to another
    within days days.

    The ith package on the conveyor belt has a weight of weights[i]. Each day,
    we load the ship with packages on the conveyor belt (in the order given by
    weights). We may not load more weight than the maximum weight capacity of the
    ship.

    Return the least weight capacity of the ship that will result in all the
    packages on the conveyor belt being shipped within days days.
Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Notes:
    - use binary search (max(weights), sum(weights))
'''
def shipWithinDays(weights: list[int], days: int) -> int:
    def check_capacity(capacity: int) -> bool:
        nonlocal weights, days
        days_needed, current_load = 1, 0
        for w in weights:
            current_load += w
            if current_load > capacity:
                days_needed += 1
                current_load = w
        return days_needed <= days

    l, r = max(weights), sum(weights)

    while l <= r:
        m = l + ((r - l) >> 1)
        if check_capacity(m):
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    w1, d1 = [1,2,3,4,5,6,7,8,9,10], 5
    w2, d2 = [3,2,2,4,1,4], 3
    w3, d3 = [1,2,3,1,1], 4

    print(shipWithinDays(w1, d1))
    print(shipWithinDays(w2, d2))
    print(shipWithinDays(w3, d3))
