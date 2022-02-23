def island_count(grid):
    count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                    count += 1
    return count

def explore(grid, r, c, visited):
    row_inbound = 0 <= r and r < len(grid)
    col_inbound = 0 <= c and c < len(grid[0])
    if not row_inbound or not col_inbound: return False
    if grid[r][c] == 'w': return False

    pos = f'{r},{c}'
    if pos in visited: return False
    visited.add(pos)
    
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)

    return True

grid = [
	['w', 'l', 'w', 'w', 'w'],
	['w', 'l', 'w', 'w', 'w'],
	['w', 'w', 'w', 'l', 'w'],
	['w', 'w', 'l', 'l', 'w'],
	['l', 'w', 'w', 'l', 'l'],
	['l', 'l', 'w', 'w', 'w']
]

print(island_count(grid))
