"""
Created Date: 2024-09-16
Qn: Given a list of 24-hour clock time points in "HH:MM" format, return the
    minimum minutes difference between any two time-points in the list.
Link: https://leetcode.com/problems/minimum-time-difference/
Notes:
    - convert to minutes and sort
"""


def findMinDifference(timePoints: list[str]) -> int:
    minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
    minutes.sort()

    res = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
    return min(res, 24 * 60 - minutes[-1] + minutes[0])


if __name__ == '__main__':
    t1 = ["23:59", "00:00"]
    t2 = ["00:00", "23:59", "00:00"]

    print(findMinDifference(t1))
    print(findMinDifference(t2))
