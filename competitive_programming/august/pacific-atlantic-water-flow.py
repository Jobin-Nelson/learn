'''
Created Date: 2022-08-31
Qn: There is an m x n rectangular island that borders both the Pacific Ocean
    and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
    and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n
    integer matrix heights where heights[r][c] represents the height above sea
    level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring
    cells directly north, south, east, and west if the neighboring cell's height is
    less than or equal to the current cell's height. Water can flow from any cell
    adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
    that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic
    oceans.
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Notes:
    - dfs from ocean to the cells using reverse flow condition
    - track cells with 2 sets for pacific and atlantic
    - return common cells in a list
'''
import pprint

def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    pac, atl = set(), set()
    R, C = len(heights), len(heights[0])

    def dfs(r, c, visited, prev_height):
        is_visited = (r, c) in visited
        col_bound = not (0 <= c < C)
        row_bound = not (0 <= r < R)

        if is_visited or col_bound or row_bound or heights[r][c] < prev_height: return

        visited.add((r, c))

        dfs(r+1, c, visited, heights[r][c])
        dfs(r-1, c, visited, heights[r][c])
        dfs(r, c+1, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])
    
    for c in range(C):
        dfs(0, c, pac, heights[0][c])
        dfs(R-1, c, atl, heights[R-1][c])

    for r in range(R):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, C-1, atl, heights[r][C-1])

    return list(pac.intersection(atl))

if __name__ == '__main__':
    h1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    h2 = [[1]]

    pprint.pprint(pacificAtlantic(h1))
    pprint.pprint(pacificAtlantic(h2))
