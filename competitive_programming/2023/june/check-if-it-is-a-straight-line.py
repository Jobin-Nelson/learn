'''
Created Date: 2023-06-05
Qn: You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
    represents the coordinate of a point. Check if these points make a straight
    line in the XY plane.
Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
Notes:
    - use straight line 
    - find delta to circumvent zero-division error
'''
def checkStraightLine(coordinates: list[list[int]]) -> bool:
    N = len(coordinates)
    if N < 2: return True
    def delta(x1: int, x2: int) -> int:
        return x1 - x2

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    deltaX = delta(x0, x1)
    deltaY = delta(y0, y1)

    for i in range(2, N):
        x, y = coordinates[i]
        if (deltaY * delta(x0, x)) != (deltaX * delta(y0, y)):
            return False
    return True

    # # Below solution fails because of zero division error
    # N = len(coordinates)
    # if N < 2: return True
    #
    # x1, y1 = coordinates[0]
    # x2, y2 = coordinates[1]
    # 
    # # Slope
    # m = (y2-y1) / (x2-x1)
    # # Find the y intercept (when x = 0)
    # c = y1 - m*x1 # y = mx + c
    #
    # for i in range(3, N):
    #     x, y = coordinates[i]
    #     if m != (y-c) / (x-0):
    #         return False
    # return True

if __name__ == '__main__':
    c1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    c2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

    print(checkStraightLine(c1))
    print(checkStraightLine(c2))
