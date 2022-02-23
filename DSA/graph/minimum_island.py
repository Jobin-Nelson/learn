def minimum_island(grid):
    min_size = len(grid) * len(grid[0])
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size

    return min_size

def explore_size(grid, r, c, visited):
    row_inbound = 0 <= r and r < len(grid)
    col_inbound = 0 <= c and c < len(grid[0])
    if not row_inbound or not col_inbound: return 0
    if grid[r][c] == 'w': return 0

    pos = f'{r},{c}'
    if pos in visited: return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r-1, c, visited)
    size += explore_size(grid, r+1, c, visited)
    size += explore_size(grid, r, c-1, visited)
    size += explore_size(grid, r, c+1, visited)

    return size

grid = [
	['w', 'l', 'w', 'w', 'w'],
	['w', 'l', 'w', 'w', 'w'],
	['w', 'w', 'w', 'l', 'w'],
	['w', 'w', 'l', 'l', 'w'],
	['l', 'w', 'w', 'l', 'l'],
	['l', 'l', 'w', 'w', 'w'],
]

print(minimum_island(grid))
