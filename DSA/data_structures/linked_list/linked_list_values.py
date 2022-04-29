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

def get_values(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def get_values_rec(node):
    res = []
    fill_values(node, res)
    return res

def fill_values(node, res):
    if node == None:
        return 
    res.append(node.val)
    fill_values(node.next, res)

if __name__ == '__main__':
    print('Getting values')
    print(get_values(a))
    print('Getting values recursively')
    print(get_values_rec(a))
        
