'''
Qn: Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
    trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change 
    the relative structure of the elements that will remain in the tree (i.e., any node's descendant 
    should remain a descendant). It can be proven that there is a unique answer.Return the root of 
    the trimmed binary search tree. Note that the root may change depending on the given bounds.
Link: https://leetcode.com/problems/trim-a-binary-search-tree/
Notes:
    - recursively check if the root.val is out of bounds if it is run the algorithm on the specific child node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trim_bst(root: TreeNode, low: int, high: int) -> TreeNode:
    if not root: return None

    if root.val > high:
        return trim_bst(root.left, low, high)
    
    if root.val < low:
        return trim_bst(root.right, low, high)
    
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root

def list_tree_rec(root: TreeNode) -> list:
    if not root: return []
    l = list_tree_rec(root.left)
    r = list_tree_rec(root.right)
    return [root.val, *l, *r]

if __name__ == '__main__':
    a1 = TreeNode(0)
    b1 = TreeNode(2)
    r1 = TreeNode(1, a1, b1)

    a2 = TreeNode(1)
    b2 = TreeNode(4)
    c2 = TreeNode(2, left=a2)
    d2 = TreeNode(0, right=c2)
    r2 = TreeNode(3, d2, b2)

    print(list_tree_rec(trim_bst(r1, 1, 2)))
    print(list_tree_rec(trim_bst(r2, 1, 3)))
