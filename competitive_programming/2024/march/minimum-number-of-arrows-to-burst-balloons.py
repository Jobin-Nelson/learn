"""
Created Date: 2024-03-18
Qn: There are some spherical balloons taped onto a flat wall that represents
    the XY-plane. The balloons are represented as a 2D integer array points
    where points[i] = [xstart, xend] denotes a balloon whose horizontal
    diameter stretches between xstart and xend. You do not know the exact
    y-coordinates of the balloons.

    Arrows can be shot up directly vertically (in the positive y-direction)
    from different points along the x-axis. A balloon with xstart and xend is
    burst by an arrow shot at x if xstart <= x <= xend. There is no limit to
    the number of arrows that can be shot. A shot arrow keeps traveling up
    infinitely, bursting any balloons in its path.

    Given the array points, return the minimum number of arrows that must be
    shot to burst all balloons.
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
Notes:
    - use intervals
"""
def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort()
    total, end = 0, float('-inf')

    for i in points:
        if i[0] > end:
            total += 1
            end = i[1]
    return total
    # res = len(points)
    # prev = points[0]
    # for cur in points[1:]:
    #     if cur[0] <= prev[1]:
    #         res -= 1
    #         prev = [cur[0], min(cur[1], prev[1])]
    #     else:
    #         prev = cur
    #
    # return res

if __name__ == '__main__':
    p1 = [[10,16],[2,8],[1,6],[7,12]]
    p2 = [[1,2],[3,4],[5,6],[7,8]]
    p3 = [[1,2],[2,3],[3,4],[4,5]]

    print(findMinArrowShots(p1))
    print(findMinArrowShots(p2))
    print(findMinArrowShots(p3))
