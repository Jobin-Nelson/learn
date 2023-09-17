'''
Created Date: 2023-09-16
Qn: You are a hiker preparing for an upcoming hike. You are given heights, a 2D
    array of size rows x columns, where heights[row][col] represents the height
    of cell (row, col). You are situated in the top-left cell, (0, 0), and you
    hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,
    0-indexed). You can move up, down, left, or right, and you wish to find a
    route that requires the minimum effort.

    A route's effort is the maximum absolute difference in heights between two
    consecutive cells of the route.

    Return the minimum effort required to travel from the top-left cell to the
    bottom-right cell.
Link: https://leetcode.com/problems/path-with-minimum-effort/
Notes:
    - use djikstra's algorithm
'''
import heapq
import sys

def minimumEffortPath(heights: list[list[int]]) -> int:
    R, C = len(heights), len(heights[0])
    min_efforts = [[sys.maxsize]* C for _ in range(R)]
    min_efforts[0][0] = 0
    pq = [(0, 0, 0)] # effort, row, col

    dirs = [1, 0, -1, 0, 1]
    visited = set()
    while pq:
        e, r, c = heapq.heappop(pq)
        # if r == R-1 and c == C-1: break
        visited.add((r, c))
        for i in range(4):
            nr, nc = r + dirs[i], c + dirs[i+1]
            if 0<=nr<R and 0<=nc<C and (nr, nc) not in visited:
                max_e = max(abs(heights[r][c] - heights[nr][nc]), e)
                if max_e < min_efforts[nr][nc]:
                    heapq.heappush(pq, (max_e, nr, nc))
                    min_efforts[nr][nc] = max_e
    return min_efforts[-1][-1]

if __name__ == '__main__':
    h1 = [[1,2,2],[3,8,2],[5,3,5]]
    h2 = [[1,2,3],[3,8,4],[5,3,5]]
    h3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

    print(minimumEffortPath(h1))
    print(minimumEffortPath(h2))
    print(minimumEffortPath(h3))
