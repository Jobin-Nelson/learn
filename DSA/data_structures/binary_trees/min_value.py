class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def min_value(root):
    small = float('inf')
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val < small: small = current.val
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return small

def min_value_rec(root):
    if root == None: return float('inf')
    return min(root.val, min_value_rec(root.left), min_value_rec(root.right))

print('Finding min value iteratively')
print(min_value(a))
print('Finding min value recursively')
print(min_value_rec(a))
