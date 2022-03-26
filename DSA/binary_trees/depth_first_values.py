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

def depth_first_values(root):
    if not root: return []
    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return result

def depth_first_values_rec(root):
    if root == None: return []
    left_values = depth_first_values_rec(root.left)
    right_values = depth_first_values_rec(root.right)
    return [root.val, *left_values, *right_values]

print('dfs, iteratively')
print(depth_first_values(a))
print('dfs recursively')
print(depth_first_values_rec(a))

