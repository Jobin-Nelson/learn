// const depthFirstPrint = (graph, source) => {
// 	const stack = [source]
// 	while (stack.length > 0) {
// 		let current = stack.pop()
// 		console.log(current)
// 		for (let neighbor of graph[current]) {
// 			stack.push(neighbor)
// 		}
// 	}
// }

// recursion 
const depthFirstPrint = (graph, source) => {
	console.log(source)
	for (let neighbor of graph[source]) {
		depthFirstPrint(graph, neighbor)
	}
}

const breadthFirstPrint = (graph, source) => {
	const queue = [source]
	while (queue.length > 0) {
		let current = queue.shift()
		console.log(current)
		for (let neighbor of graph[current]) {
			queue.push(neighbor)
		}
	}
}

const graph = {
	a: ['b', 'c'],
	b: ['d'],
	c: ['e'],
	d: ['f'],
	e: [],
	f: [],
}

console.log('Depth first traversal')
depthFirstPrint(graph, 'a')

console.log('Breadth first traversal')
breadthFirstPrint(graph, 'a')

