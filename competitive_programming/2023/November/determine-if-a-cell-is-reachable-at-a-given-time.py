'''
Created Date: 2023-11-08
Qn: Can you solve this real interview question? Determine if a Cell Is
    Reachable at a Given Time - You are given four integers sx, sy, fx, fy, and
    a non-negative integer t.

    In an infinite 2D grid, you start at the cell (sx, sy). Each second, you
    must move to any of its adjacent cells.

    Return true if you can reach cell (fx, fy) after exactly t seconds, or
    false otherwise.

    A cell's adjacent cells are the 8 cells around it that share at least one
    corner with it. You can visit the same cell several times.
Link: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
Notes:
    - return t >= max(height_diff, width_diff)
    - edge case is w == 0 h == 0 and t == 1
'''
def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    width = abs(sx - fx)
    height = abs(sy - fy)
    if width == 0 and height == 0 and t == 1: return False
    return t >= max(height, width)

if __name__ == '__main__':
    sx1, sy1, fx1, fy1, t1 = 2, 4, 7, 7, 6
    sx2, sy2, fx2, fy2, t2 = 3, 1, 7, 3, 3
    sx3, sy3, fx3, fy3, t3 = 2, 4, 7, 7, 6

    print(isReachableAtTime(sx1, sy1, fx1, fy1, t1))
    print(isReachableAtTime(sx2, sy2, fx2, fy2, t2))
    print(isReachableAtTime(sx3, sy3, fx3, fy3, t3))
