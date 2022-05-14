class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def max_path_sum(root):
    if root == None: return float('-inf')
    if root.left == None and root.right == None: return root.val
    max_child_path_sum = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.val + max_child_path_sum

print('Finding the max path sum recursively')
print(max_path_sum(a))
