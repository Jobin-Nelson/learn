"""
Created Date: 2023-12-21
Qn: Given n points on a 2D plane where points[i] = [xi, yi], Return the widest
    vertical area between two points such that no points are inside the area.

    A vertical area is an area of fixed-width extending infinitely along the
    y-axis (i.e., infinite height). The widest vertical area is the one with
    the maximum width.

    Note that points on the edge of a vertical area are not considered included
    in the area.
Link: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
Notes:
    - use sort and max between two consecutive elements
"""
def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    xs = sorted(p[0] for p in points)
    res = 0
    for i in range(1, len(points)):
        res = max(res, xs[i] - xs[i-1])
    return res

if __name__ == '__main__':
    p1 = [[8,7],[9,9],[7,4],[9,7]]
    p2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

    print(maxWidthOfVerticalArea(p1))
    print(maxWidthOfVerticalArea(p2))
