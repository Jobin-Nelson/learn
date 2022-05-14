'''
Qn: Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Notes:
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    if root == None: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

if __name__ == '__main__':
    r4 = TreeNode(15)
    r5 = TreeNode(7)
    r2 = TreeNode(9)
    r3 = TreeNode(20, r4, r5)
    r1 = TreeNode(3, r2, r3)

    s2 = TreeNode(2)
    s1 = TreeNode(1, None, s2)

    print(max_depth(r1))
    print(max_depth(s1))
