class Node {
	constructor(val) {
		this.val = val
		this.next = null
	}
}

const a = new Node(2)
const b = new Node(8)
const c = new Node(3)
const d = new Node(-1)
const e = new Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

const getSum = (node) => {
	let sum = 0
	while (node != null) {
		sum += node.val
		node = node.next
	}
	return sum
}

const getSumRec = (node) => {
	if (node == null) return 0
	return node.val + getSumRec(node.next)
}

console.log('Getting sum')
console.log(getSum(a))
console.log('Getting sum recursively')
console.log(getSumRec(a))

