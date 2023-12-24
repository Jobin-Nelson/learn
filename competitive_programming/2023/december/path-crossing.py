"""
Created Date: 2023-12-23
Qn: Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each
    representing moving one unit north, south, east, or west, respectively. You
    start at the origin (0, 0) on a 2D plane and walk on the path specified by
    path.

    Return true if the path crosses itself at any point, that is, if at any
    time
you are on a location you have previously visited. Return false otherwise.
Link: https://leetcode.com/problems/path-crossing/
Notes:
    - use hashset to check crossing
"""
def isPathCrossing(path: str) -> bool:
    u, r = 0, 0
    visited = set()
    visited.add((u, r))
    for d in path:
        if d == 'N':
            u += 1
        elif d == 'S':
            u -= 1
        elif d == 'E':
            r += 1
        elif d == 'W':
            r -= 1
        if (u, r) in visited: return True
        visited.add((u, r))
    return False

if __name__ == '__main__':
    p1 = "NES"
    p2 = "NESWW"

    print(isPathCrossing(p1))
    print(isPathCrossing(p2))
