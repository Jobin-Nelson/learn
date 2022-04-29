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

def find(node, target):
    while node:
        if node.val == target:
            return True
        node = node.next

    return False

def find_rec(node, target):
    if node == None:
        return False
    if node.val == target:
        return True
    return find_rec(node.next, target)

if __name__ == '__main__':
    print('Searching for target')
    print(find(a, 'C'))
    print('Searching for target recursively')
    print(find(a, 'D'))

