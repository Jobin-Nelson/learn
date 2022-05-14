'''
Qn: Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Notes:
- preorder list gives you the root node
- index of the root node in the inorder list gives how you can split preorder list into left and right 
- return the node recursively to build the binary tree using these lists
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root

def depth_first_values_rec(root):
    if root == None: return []
    left_values = depth_first_values_rec(root.left)
    right_values = depth_first_values_rec(root.right)
    return [root.val, *left_values, *right_values]

if __name__ == '__main__':
    p1, o1 = [3,9,20,15,7], [9,3,15,20,7]
    p2, o2 = [-1], [-1]

    print(depth_first_values_rec(build_tree(p1, o1)))
    print(depth_first_values_rec(build_tree(p2, o2)))
