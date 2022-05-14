'''
Qn: The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Notes: 
- dfs from the border and adding to respective pacific and atlantic sets
- return the list of common values on both sets
'''

def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or
            r < 0 or c < 0 or r == rows or c == cols or
            heights[r][c] < prev_height):
            return 
        visited.add((r, c))
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows-1, c, atl, heights[rows-1][c])
    
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols-1, atl, heights[r][cols-1])
    
    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res

if __name__ == '__main__':
    h1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    h2 = [[2,1],[1,2]]
    print(pacific_atlantic(h1))
    print(pacific_atlantic(h2))