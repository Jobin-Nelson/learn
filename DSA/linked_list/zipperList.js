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

const x = new Node('X')
const y = new Node('Y')
const z = new Node('Z')

x.next = y
y.next = z

const printLinkedList = (head) => {
	let current = head
	while (current != null) {
		console.log(current.val)
		current = current.next
	}
}

const zipperList = (node1, node2) => {
	let tail = node1
	let current1 = node1.next
	let current2 = node2
	let count = 0
	while (current1 != null && current2 != null) {
		if (count%2 === 0) {
			tail.next = current2
			current2 = current2.next
		}
		else {
			tail.next = current1
			current1 = current1.next
		}
		count += 1
		tail = tail.next
	}

	if (current1 != null) tail.next = current1
	if (current2 != null) tail.next = current2
	return node1
}

const zipperListRec = (node1, node2) => {
	if (node1 === null && node2 === null) return null
	if (node1 === null) return node2
	if (node2 === null) return node1

	const nex1 = node1.next
	const nex2 = node2.next
	node1.next = node2
	node2.next = zipperListRec(nex1, nex2)
	return node1
}

console.log('Before zipping')
console.log('First node')
printLinkedList(a)
console.log('Second node')
printLinkedList(x)
console.log('After zipping')
printLinkedList(zipperList(a, x))
console.log('After zipping recursively')
const u = new Node('U')
const v = new Node('V')
const w = new Node('W')

u.next = v
v.next = w
printLinkedList(zipperListRec(a, u))


