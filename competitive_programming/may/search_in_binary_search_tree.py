'''
Qn: Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null
Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Notes:
    - recurse till you find the value or hit the end of the tree and return the node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_bst(root: TreeNode, val: int) -> TreeNode:
    if not root: return None
    if root.val > val:
        res = search_bst(root.left, val)
    elif root.val < val:
        res = search_bst(root.right, val)
    else:
        res = root
    return res

def print_tree_rec(root: TreeNode):
    if not root: return []
    l = print_tree_rec(root.left)
    r = print_tree_rec(root.right)
    return [root.val, *l, *r]

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(7)
    d = TreeNode(2, a, b)
    r = TreeNode(4, d, c)
    print(print_tree_rec(search_bst(r, 2)))
    print(print_tree_rec(search_bst(r, 5)))
