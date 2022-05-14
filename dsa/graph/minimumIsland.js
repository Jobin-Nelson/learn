const minimumIsland = (grid) => {
	let minSize = grid.length * grid[0].length
	const visited = new Set()
	for (let r=0; r<grid.length; r++) {
		for (let c=0; c<grid[0].length; c++) {
			const size = exploreSize(grid, r, c, visited)
			if (size > 0 && size < minSize) {
				minSize = size
			}
		}
	}
	return minSize
}

const exploreSize = (grid, r, c, visited) => {
	const rowInbound = 0 <= r && r < grid.length
	const colInbound = 0 <= c && c < grid[0].length
	if (!rowInbound || !colInbound) return 0
	if (grid[r][c] === 'w') return 0

	const pos = r + ',' + c
	if (visited.has(pos)) return 0
	visited.add(pos)

	let size = 1
	size += exploreSize(grid, r-1, c, visited)
	size += exploreSize(grid, r+1, c, visited)
	size += exploreSize(grid, r, c-1, visited)
	size += exploreSize(grid, r, c+1, visited)

	return size
}

const grid = [
	['w', 'l', 'w', 'w', 'w'],
	['w', 'l', 'w', 'w', 'w'],
	['w', 'w', 'w', 'l', 'w'],
	['w', 'w', 'l', 'l', 'w'],
	['l', 'w', 'w', 'l', 'l'],
	['l', 'l', 'w', 'w', 'w'],
]

console.log(minimumIsland(grid))
