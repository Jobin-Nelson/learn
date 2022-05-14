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

const find = (node, target) => {
	while (node != null) {
		if (node.val === target) return true
		node = node.next
	}
	return false
}

const findRec = (node, target) => {
	if (node === null) return false
	if (node.val === target) return true
	return findRec(node.next, target)
}

console.log('Searching for target')
console.log(find(a, 'C'))
console.log('Searching for target recursively')
console.log(findRec(a, 'D'))
	
