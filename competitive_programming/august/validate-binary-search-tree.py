'''
Created Date: 11-08-2022
Qn: Given the root of a binary tree, determine if it is a valid binary search
    tree (BST).

    A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than
          the node's key. 
        - The right subtree of a node contains only nodes with keys greater
          than the node's key. 
        - Both the left and right subtrees must also be binary search trees.
Link: https://leetcode.com/problems/validate-binary-search-tree/
Notes:
- Same level comparison
- Track two variables left and right and update it with the current value
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(left, node, right):
        if not node: return True
        if not (left < node.val < right): return False
        return valid(left, node.left, node.val) and valid(node.val, node.right, right)
    return valid(float('-inf'), root, float('inf'))

if __name__ == '__main__':
    a1 = TreeNode(1)
    b1 = TreeNode(3)
    r1 = TreeNode(2, a1, b1)

    a2 = TreeNode(1)
    b2 = TreeNode(3)
    c2 = TreeNode(6)
    d2 = TreeNode(4, b2, c2)
    r2 = TreeNode(5, a2, d2)
    print(isValidBST(r1))
    print(isValidBST(r2))
