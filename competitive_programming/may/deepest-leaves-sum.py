'''
Qn: Given the root of a binary tree, 
    return the sum of values of its deepest leaves.
Link: https://leetcode.com/problems/deepest-leaves-sum/
Notes:
- bfs level order traversal and get sum at each level
'''
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    if not root: return 0
    q = deque([root])
    while q:
        s = 0
        q_len = len(q)
        for _ in range(q_len):
            cur = q.popleft()
            s += cur.val
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
    return s

if __name__ == '__main__':
    a1 = TreeNode(7)
    b1 = TreeNode(8)
    c1 = TreeNode(4, a1)
    d1 = TreeNode(5)
    e1 = TreeNode(6, right=b1)
    f1 = TreeNode(2, c1, d1)
    g1 = TreeNode(3, right=e1)
    r1 = TreeNode(1, f1, g1)

    a2 = TreeNode(9)
    b2 = TreeNode(1)
    c2 = TreeNode(4)
    d2 = TreeNode(5)
    e2 = TreeNode(2, a2)
    f2 = TreeNode(7, b2, c2)
    g2 = TreeNode(1)
    h2 = TreeNode(3, right=d2)
    i2 = TreeNode(7, e2, f2)
    j2 = TreeNode(8, b2, h2)
    r2 = TreeNode(6, i2, j2)

    print(deepestLeavesSum(r1))
    print(deepestLeavesSum(r2))
