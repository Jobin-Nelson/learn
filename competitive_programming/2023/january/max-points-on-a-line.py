'''
Created Date: 2023-01-08
Qn: Given an array of points where points[i] = [xi, yi] represents a point on
    the X-Y plane, return the maximum number of points that lie on the same
    straight line.
Link: https://leetcode.com/problems/max-points-on-a-line/
Notes:
    - find tan2 between every two points
    - and add the number of same tan2 values using hashmap
    - return the maximum count
'''
import math
from collections import defaultdict

def maxPoints(points: list[list[int]]) -> int:
    N = len(points)
    if N == 1: return 1

    res = 2
    for i in range(N):
        cnt = defaultdict(int)
        for j in range(N):
            if i == j: continue
            cnt[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
        res = max(res, max(cnt.values()) + 1)
    return res

if __name__ == '__main__':
    p1 = [[1,1],[2,2],[3,3]]
    p2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

    print(maxPoints(p1))
    print(maxPoints(p2))
