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

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def reverse_list(node):
    pre = None

    while node:
        nex = node.next
        node.next = pre
        pre = node
        node = nex
    return pre

def reverse_list_rec(node, prev=None):
    if node == None:
        return pre
    nex = node.next
    node.next = prev
    prev = node
    return reverse_list_rec(nex, prev)

if __name__ == '__main__':
    print('Before reversing')
    print_linked_list(a)
    print('After reversing')
    print_linked_list(reverse_list(a))    
    print('After reversing recursively')
    print_linked_list(reverse_list(d))
