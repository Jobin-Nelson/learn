class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def tree_includes(root, target):
    if root == None: return []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current.val == target: return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

def tree_includes_rec(root, target):
    if root == None: return False
    if root.val == target: return True
    return tree_includes_rec(root.left, target) or tree_includes_rec(root.right, target)

print('Searching iteratively')
print(tree_includes(a, 'e'))
print('Searching recursively')
print(tree_includes_rec(a, 'e'))
