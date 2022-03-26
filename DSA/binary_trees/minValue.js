class Node {
	constructor(val) {
		this.val = val
		this.left = null
		this.right = null
	}
}

const a = new Node(3)
const b = new Node(11)
const c = new Node(4)
const d = new Node(4)
const e = new Node(2)
const f = new Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

const minValue = (root) => {
	const stack = [root]
	let small = Infinity

	while (stack.length > 0) {
		const current = stack.pop()
		if (current.val < small) small = current.val
		if (current.left) stack.push(current.left)
		if (current.right) stack.push(current.right)
	}
	return small
}

const minValueRec = (root) => {
	if (root === null) return Infinity
	let leftMin = minValueRec(root.left)
	let rightMin = minValueRec(root.right)
	return Math.min(root.val, leftMin, rightMin)
}

console.log('Finding min value iteratively')
console.log(minValue(a))
console.log('Finding min value recursively')
console.log(minValueRec(a))
	
