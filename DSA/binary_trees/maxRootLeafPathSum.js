class Node {
	constructor(val) {
		this.val = val
		this.left = null
		this.right = null
	}
}

const a = new Node(5)
const b = new Node(11)
const c = new Node(3)
const d = new Node(4)
const e = new Node(2)
const f = new Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

const maxPathSum = (root) => {
	if (root === null) return -Infinity 
	if (root.left === null && root.right === null) return root.val
	const maxChildPathSum = Math.max(maxPathSum(root.left), maxPathSum(root.right))
	return root.val + maxChildPathSum
}

console.log('Finding max path sum recursively')
console.log(maxPathSum(a))
