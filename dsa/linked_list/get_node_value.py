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

def get_node(node, index):
    count = 0
    while node:
        if count == index:
            return node.val
        node = node.next
        count += 1
    return -1 

def get_node_rec(node, index):
    if node == None:
        return -1
    if index == 0:
        return node.val
    return get_node_rec(node.next, index-1)

if __name__ == '__main__':
    print('Getting node')
    print(get_node(a, 2))
    print('Getting node recursively')
    print(get_node_rec(a, 2))
