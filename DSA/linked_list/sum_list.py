class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def get_sum(node):
    s = 0
    while node:
        s += node.val
        node = node.next
    return s

def get_sum_rec(node):
    if node == None:
        return 0
    return node.val + get_sum_rec(node.next)

if __name__ == '__main__':
    print('Getting sum')
    print(get_sum(a))
    print('Getting sum recursively')
    print(get_sum_rec(a))
