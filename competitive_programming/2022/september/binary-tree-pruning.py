'''
Created Date: 2022-09-06
Qn: Given the root of a binary tree, return the same tree where every subtree
    (of the given tree) not containing a 1 has been removed.

    A subtree of a node node is node plus every node that is a descendant of node.
Link: https://leetcode.com/problems/binary-tree-pruning/
Notes:
    - dfs and prune nodes that doesn't have or descendant's having 1
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
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level)
        return str(result)

def pruneTree(root: TreeNode | None) -> TreeNode | None:
    # if not root: return None
    # def prune(node):
    #     if not node: return False
    #     current_res = node.val == 1
    #     left_res = prune(node.left)
    #     right_res = prune(node.right)
    #     if not left_res: node.left = None
    #     if not right_res: node.right = None
    #     return current_res or left_res or right_res
    # prune(root)
    # return root
    if root is None: return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if root.left is None and root.right is None and root.val == 0: return None
    return root

if __name__ == '__main__':
    a1 = TreeNode(0)
    b1 = TreeNode(1)
    c1 = TreeNode(0, a1, b1)
    r1 = TreeNode(1, None, c1)

    a2 = TreeNode(0)
    b2 = TreeNode(0)
    c2 = TreeNode(0)
    d2 = TreeNode(1)
    e2 = TreeNode(0, a2, b2)
    f2 = TreeNode(1, c2, d2)
    r2 = TreeNode(1, e2, f2)

    a3 = TreeNode(0)
    b3 = TreeNode(1, a3)
    c3 = TreeNode(1)
    d3 = TreeNode(0)
    e3 = TreeNode(1)
    f3 = TreeNode(1, b3, c3)
    g3 = TreeNode(0, d3, e3)
    r3 = TreeNode(1, f3, g3)

    print(pruneTree(r1))
    print(pruneTree(r2))
    print(pruneTree(r3))
