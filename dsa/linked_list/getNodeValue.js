class Node {
	constructor(val) {
		this.val = val
		this.next = null
	}
}

const a = new Node('A')
const b = new Node('B')
const c = new Node('C')
const d = new Node('D')

a.next = b
b.next = c
c.next = d

const getNode = (node, index) => {
	let count = 0
	while (node != null) {
		if (count === index) return node.val
		node = node.next
		count += 1
	}
	return -1
}

const getNodeRec = (node, index) => {
	if (node === null) return -1
	if (index === 0) return node.val
	return getNodeRec(node.next, index-1)
}

console.log('Getting node')
console.log(getNode(a, 2))
console.log('Getting node recursively')
console.log(getNodeRec(a, 2))
