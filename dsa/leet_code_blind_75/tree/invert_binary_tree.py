'''
Qn: Given the root of a binary tree, invert the tree, and return its root
Link: https://leetcode.com/problems/invert-binary-tree/
Notes:
- dfs till you hit None and switch when you return
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if not root: return root
    temp = invert_tree(root.right)
    root.right = invert_tree(root.left)
    root.left = temp
    return root



def depth_first_values_rec(root):
    if root == None: return []
    left_values = depth_first_values_rec(root.left)
    right_values = depth_first_values_rec(root.right)
    return [root.val, *left_values, *right_values]


if __name__ == '__main__':
    a1 = TreeNode(1)
    b1 = TreeNode(3)
    c1 = TreeNode(6)
    d1 = TreeNode(9)
    e1 = TreeNode(2, a1, b1)
    f1 = TreeNode(7, c1, d1)
    r1 = TreeNode(4, e1, f1)

    
    a2 = TreeNode(1)
    b2 = TreeNode(3)
    r2 = TreeNode(2, a2, b2)

    print('Before inverting')
    print(depth_first_values_rec(r1))
    print(depth_first_values_rec(r2))


    print('\n\nAfter inverting')
    print(depth_first_values_rec(invert_tree(r1)))
    print(depth_first_values_rec(invert_tree(r2)))
    
