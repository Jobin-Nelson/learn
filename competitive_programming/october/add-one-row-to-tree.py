'''
Created Date: 2022-10-05
Qn: Given the root of a binary tree and two integers val and depth, add a row
    of nodes with value val at the given depth depth.

    Note that the root node is at depth 1.

    The adding rule is:

    - Given the integer depth, for each not null tree node cur at the depth
      depth - 1, create two tree nodes with value val as cur's left subtree
      root and right subtree root. 
    - cur's original left subtree should be the left subtree of the new left
      subtree root. 
    - cur's original right subtree should be the right subtree of the new right
      subtree root. 
    - If depth == 1 that means there is no depth depth - 1 at all, then create
      a tree node with value val as the new root of the whole original tree,
      and the original tree is the new root's left subtree.
Link: https://leetcode.com/problems/add-one-row-to-tree/
Notes:
    - dfs till depth-1
    - insert new treenode in between parent and child node
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        res = []
        q = deque()
        root = self
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return str(res)

def addOneRow(root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
    def dfs(node, depth, d):
        if not node: return None
        if depth == 1:
            return TreeNode(val, left=node)
        if depth-1 == d:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
            return node
        dfs(node.left, depth, d+1)
        dfs(node.right, depth, d+1)
        return node
    return dfs(root, depth, 1)

if __name__ == '__main__':
    a1 = TreeNode(3)
    b1 = TreeNode(1)
    c1 = TreeNode(5)
    d1 = TreeNode(2, a1, b1)
    e1 = TreeNode(6, c1)
    r1 = TreeNode(4, d1, e1)
    val1, dep1 = 1, 2

    a2 = TreeNode(3)
    b2 = TreeNode(1)
    d2 = TreeNode(2, a2, b2)
    r2 = TreeNode(4, d2)
    val2, dep2 = 1, 3

    print(addOneRow(r1, val1, dep1))
    print(addOneRow(r2, val2, dep2))

