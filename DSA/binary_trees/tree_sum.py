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

def tree_sum(root):
    if root == None: return 0
    sum = 0
    queue = [root]

    while queue:
        current = queue.pop(0)
        sum += current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum

def tree_sum_rec(root):
    if root == None: return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

print('Getting sum iteratively')
print(tree_sum(a))
print('Getting sum recursively')
print(tree_sum_rec(a))

