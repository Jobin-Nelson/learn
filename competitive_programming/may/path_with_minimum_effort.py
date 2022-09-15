'''
Qn: Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
Link: https://leetcode.com/problems/path-with-minimum-effort/
Notes:
    - try different values from 0 to max of heights
    - binary searh your way down to the smallest value that completes the path
'''
def minimum_effort_path(heights: list[list[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(k, x, y):
        visited.add((x, y))
        for dx, dy in dirs:
            new_x, new_y = x+dx, y+dy
            if 0<=new_x<rows and 0<=new_y<cols and (new_x, new_y) not in visited:
                new_k = abs(heights[x][y] - heights[new_x][new_y])
                if new_k <= k:
                    dfs(k, new_x, new_y)

    mn, mx = -1, max([heights[r][c] for c in range(cols) for r in range(rows)])
    while mn+1 < mx:
        mid = (mx + mn)// 2
        visited = set()
        dfs(mid, 0, 0)
        if (rows-1, cols-1) in visited:
            mx = mid
        else:
            mn = mid
    return mx

if __name__ == '__main__':
    h1 = [[1,2,2],[3,8,2],[5,3,5]]
    h2 = [[1,2,3],[3,8,4],[5,3,5]]
    h3 = [
            [1,2,1,1,1],
            [1,2,1,2,1],
            [1,2,1,2,1],
            [1,2,1,2,1],
            [1,1,1,2,1]]
    print(minimum_effort_path(h1))
    print(minimum_effort_path(h2))
    print(minimum_effort_path(h3))
    
