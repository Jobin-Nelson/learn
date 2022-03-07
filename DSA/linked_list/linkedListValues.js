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

const getValues = (node) => {
	const res = []

	while (node != null) {
		res.push(node.val)
		node = node.next
	}
	return res
}

const getValuesRec = (node) => {
	const res = []
	fillValues(node, res)
	return res
}

const fillValues = (node, res) => {
	if (node === null) return
	res.push(node.val)
	fillValues(node.next, res)
}

console.log('getting values')
console.log(getValues(a))
console.log('getting values recursively')
console.log(getValuesRec(a))


