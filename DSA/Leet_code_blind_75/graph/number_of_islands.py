'''
Qn: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Link: https://leetcode.com/problems/number-of-islands/
Notes: 
- bfs without queue since we need to only return a bool value increment if true
'''
def num_islands(grid):
    count = 0
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count

def explore(grid, r, c, visited):
    row_outbound = 0 <= r and r < len(grid)
    col_outbound = 0 <= c and c < len(grid[0])
    if not row_outbound or not col_outbound or grid[r][c] == '0':
        return False

    pos = f'{r}, {c}'
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True
    

if __name__ == '__main__':
    g1 =  [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    g2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(num_islands(g1))
    print(num_islands(g2))