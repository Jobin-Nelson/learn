'''
Created Date: 2023-07-26
Qn: You are given a floating-point number hour, representing the amount of time
    you have to reach the office. To commute to the office, you must take n
    trains in sequential order. You are also given an integer array dist of
    length n, where dist[i] describes the distance (in kilometers) of the ith
    train ride.

    Each train can only depart at an integer hour, so you may need to wait in
    between each train ride.

        For example, if the 1st train ride takes 1.5 hours, you must wait for
        an additional 0.5 hours before you can depart on the 2nd train ride at
        the 2 hour mark.

    Return the minimum positive integer speed (in kilometers per hour) that all
    the trains must travel at for you to reach the office on time, or -1 if it
    is impossible to be on time.

    Tests are generated such that the answer will not exceed 107 and hour will
    have at most two digits after the decimal point.
Link: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
Notes:
    - use binary search
'''
import math

def minSpeedOnTime(dist: list[int], hour: float) -> int:
    def timeRequired(speed: int) -> float:
        time = 0.0
        N = len(dist)
        for i, d in enumerate(dist):
            t = d / speed
            time += t if i == N-1 else math.ceil(t)
        return time
    l, r = 1, int(1e7)
    minSpeed = -1
    while l <= r:
        m = (l + r) // 2
        if timeRequired(m) <= hour:
            minSpeed = m
            r = m -1
        else:
            l = m + 1
    return minSpeed

if __name__ == '__main__':
    d1, h1 = [1,3,2], 6
    d2, h2 = [1,3,2], 2.7
    d3, h3 = [1,3,2], 1.9

    assert minSpeedOnTime(d1, h1) == 1
    assert minSpeedOnTime(d2, h2) == 3
    assert minSpeedOnTime(d3, h3) == -1
