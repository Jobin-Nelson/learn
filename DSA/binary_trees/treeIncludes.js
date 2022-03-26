class Node {
	constructor(val) {
		this.val = val
		this.left = null
		this.right = null
	}
}

const a = new Node('a')
const b = new Node('b')
const c = new Node('c')
const d = new Node('d')
const e = new Node('e')
const f = new Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

const treeIncludes = (root, target) => {
	if (root === null) return false
	const queue = [root]

	while (queue.length > 0) {
		const current = queue.shift()
		if (current.val === target) return true
		if (current.left) queue.push(current.left)
		if (current.right) queue.push(current.right)
	}
	return false
}

const treeIncludesRec = (root, target) => {
	if (root === null) return false
	if (root.val === target) return true
	return treeIncludesRec(root.left, target) || treeIncludesRec(root.right, target)
}

console.log('Searching iteratively')
console.log(treeIncludes(a, 'e'))
console.log('Searching recursively')
console.log(treeIncludesRec(a, 'e'))
