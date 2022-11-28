'''
Created Date: 12-08-2022
Qn: Given a binary search tree (BST), find the lowest common ancestor (LCA)
    node of two given nodes in the BST.
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Notes:
    - leverage the nature of BST (left values are smaller and right values are bigger)
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        q = deque()
        q.append(self)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: result.extend(level)
        return str(result)

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else: return root

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(0)
    d = TreeNode(4, a, b)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(2, c, d)
    h = TreeNode(8, e, f)
    r = TreeNode(6, g, h)

    print(lowestCommonAncestor(r, g, h))
    print(lowestCommonAncestor(r, g, d))

