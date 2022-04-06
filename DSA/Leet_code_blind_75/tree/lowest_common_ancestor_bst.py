'''
Qn: Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Notes:
- if both values are lesser than the current check left tree
- if both values are bigger than the current check right tree
- else return the current node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root

    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur.val

if __name__ == '__main__':
    a1 = TreeNode(0)
    b1 = TreeNode(3)
    c1 = TreeNode(5)
    d1 = TreeNode(7)
    e1 = TreeNode(9)
    f1 = TreeNode(4, b1, c1)
    g1 = TreeNode(2, a1, f1)
    h1 = TreeNode(8, d1, e1)
    r1 = TreeNode(6, g1, h1)

    print(lowest_common_ancestor(r1, g1, h1))
    print(lowest_common_ancestor(r1, g1, f1))
