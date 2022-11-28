'''
Created Date: 2022-11-17
Qn: Given the coordinates of two rectilinear rectangles in a 2D plane, return
    the total area covered by the two rectangles.

    The first rectangle is defined by its bottom-left corner (ax1, ay1) and its
    top-right corner (ax2, ay2).

    The second rectangle is defined by its bottom-left corner (bx1, by1) and
    its top-right corner (bx2, by2).
Link: https://leetcode.com/problems/rectangle-area/
Notes:
    - rec1 area + rec2 area - overlap area
'''
def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    # rec1 + rec2 - common area
    def area(x1: int, y1: int, x2: int, y2: int) -> int:
        return (x1 - x2) * (y1 - y2)
    def overlap(l1: int, l2: int, r1: int, r2: int) -> int:
        return max(min(r1, r2) - max(l1, l2), 0)
    return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - overlap(ax1, bx1, ax2, bx2) * overlap(ay1, by1, ay2, by2)

if __name__ == '__main__':
    x1, y1 = -3, 0
    x2, y2 = 3, 4
    p1, q1 = 0, -1
    p2, q2 = 9, 2

    print(computeArea(x1, y1, x2, y2, p1, q1, p2, q2))

    x1, y1 = -2, -2
    x2, y2 = 2, 2
    p1, q1 = -2, -2
    p2, q2 = 2, 2

    print(computeArea(x1, y1, x2, y2, p1, q1, p2, q2))
