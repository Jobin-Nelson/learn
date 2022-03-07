class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

x = Node('X')
y = Node('Y')
z = Node('Z')

x.next = y
y.next = z

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def zipper_list(node1, node2):
    count = 0
    tail = node1
    current1 = node1.next
    current2 = node2

    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        count += 1
        tail = tail.next

    if current1: tail.next = current1
    if current2: tail.next = current2
    return node1

def zipper_list_rec(node1, node2):
    if node1 == None and node2 == None:
        return None
    if node1 == None:
        return node2
    if node2 == None:
        return node1

    nex1 = node1.next
    nex2 = node2.next
    node1.next = node2
    node2.next = zipper_list_rec(nex1, nex2)
    return node1


if __name__ == '__main__':
    print('Before zipping')
    print('First node')
    print_linked_list(a)
    print('Second node')
    print_linked_list(x)
    print('After zipping')
    print_linked_list(zipper_list(a, x))
    print('After zipping recursively')
    u = Node('U')
    v = Node('V')
    w = Node('W')

    u.next = v
    v.next = w

    print_linked_list(zipper_list(a, u))
