const hasPathDepth = (graph, src, dst) => {
	if (src === dst) return true
	for (let neighbor of graph[src]) {
		if (hasPathDepth(graph, neighbor, dst) === true) {
			return true
		}
	}
	return false
}

const hasPathBreadth = (graph, src, dst) => {
	const queue = [src]
	while (queue.length > 0) {
		const current = queue.shift()
		if (current === dst) return true
		for (let neighbor of graph[current]) {
			queue.push(neighbor)
		}
	}
	return false
}

graph = {
	f: ['g', 'i'],
	g: ['h'],
	h: [],
	i: ['g', 'k'],
	j: ['i'],
	k: []
}

console.log(hasPathDepth(graph, 'f', 'k'))
console.log(hasPathBreadth(graph, 'f', 'k'))
