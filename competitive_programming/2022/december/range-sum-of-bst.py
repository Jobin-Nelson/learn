'''
Created Date: 2022-12-07
Qn: Given the root node of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value in the inclusive range 
    [low, high].
Link: https://leetcode.com/problems/range-sum-of-bst/
Notes:
    - use dfs
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        cur = self
        q = deque([cur])
        res = []

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def rangeSumBST(root: TreeNode | None, low: int, high: int) -> int:
    if not root: return 0

    elif root.val < low:
        return rangeSumBST(root.right, low, high)
    elif root.val > high:
        return rangeSumBST(root.left, low, high)
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)

if __name__ == '__main__':
    a1 = TreeNode(3)
    b1 = TreeNode(7)
    c1 = TreeNode(18)
    d1 = TreeNode(5, a1, b1)
    e1 = TreeNode(15, c1)
    r1 = TreeNode(10, d1, e1)

    g2 = TreeNode(1)
    h2 = TreeNode(6)
    a2 = TreeNode(3, g2)
    b2 = TreeNode(7, h2)
    f2 = TreeNode(13)
    c2 = TreeNode(18)
    d2 = TreeNode(5, a2, b2)
    e2 = TreeNode(15, f2, c2)
    r2 = TreeNode(10, d2, e2)

    print(rangeSumBST(r1, 7, 15))
    print(rangeSumBST(r2, 6, 10))
