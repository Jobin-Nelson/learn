"""
Created Date: 2023-12-03
Qn: On a 2D plane, there are n points with integer coordinates points[i] = [xi,
    yi]. Return the minimum time in seconds to visit all the points in the
    order given by points.

    You can move according to these rules:

        - In 1 second, you can either:
            - move vertically by one unit,
            - move horizontally by one unit, or
            - move diagonally sqrt(2) units (in other words, move one unit
              vertically then one unit horizontally in 1 second).
        - You have to visit the points in the same order as they appear in the
          array. 
        - You are allowed to pass through points that appear later in the
          order, but these do not count as visits.

Link: https://leetcode.com/problems/minimum-time-visiting-all-points/
Notes:
"""
from functools import reduce

def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    res = 0
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        res += max(abs(x2-x1), abs(y2-y1))
    return res
    # return reduce(lambda a, b: max(abs(a[1]-a[0]), abs(b[1]-b[0])), points)

if __name__ == '__main__':
    p1 = [[1,1],[3,4],[-1,0]]
    p2 = [[3,2],[-2,2]]

    print(minTimeToVisitAllPoints(p1))
    print(minTimeToVisitAllPoints(p2))
