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

const reverseList = (node) => {
	let pre = null

	while (node != null) {
		let nex = node.next
		node.next = pre
		pre = node
		node = nex
	}
	return pre
}

const printLinkedList = (head) => {
	let current = head
	while (current != null) {
		console.log(current.val)
		current = current.next
	}
}

const reverseListRec = (node, pre=null) => {
	if (node === null) return pre
	nex = node.next
	node.next = pre
	pre = node
	return reverseListRec(nex, pre)
}
	
console.log('Before reversing')
printLinkedList(a)
console.log('After reversing')
printLinkedList(reverseList(a))
console.log('After reversing recursively')
printLinkedList(reverseListRec(d))
