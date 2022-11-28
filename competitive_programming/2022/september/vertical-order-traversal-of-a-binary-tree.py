'''
Created Date: 2022-09-04
Qn: Given the root of a binary tree, calculate the vertical order traversal of
    the binary tree.

    For each node at position (row, col), its left and right children will be at
    positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
    the tree is at (0, 0).

    The vertical order traversal of a binary tree is a list of top-to-bottom
    orderings for each column index starting from the leftmost column and ending on
    the rightmost column. There may be multiple nodes in the same row and same
    column. In such a case, sort these nodes by their values.

    Return the vertical order traversal of the binary tree.
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Notes:
    - hashmap with keys as columns
'''
from collections import defaultdict
from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root: TreeNode | None) -> list[list[int]]:
    map = defaultdict(list)

    def dfs(node, x, y):
        if not node: return
        heappush(map[x], (y, node.val))
        dfs(node.left, x-1, y+1)
        dfs(node.right, x+1, y+1)
    dfs(root, 0, 0)

    output = []

    for _, v in sorted(map.items()):
        tmp = []
        while v:
            cand = heappop(v)
            tmp.append(cand[1])
        output.append(tmp)
    return output

if __name__ == '__main__':
    a1 = TreeNode(9)
    b1 = TreeNode(15)
    c1 = TreeNode(7)
    d1 = TreeNode(20, b1, c1)
    r1 = TreeNode(3, a1, d1)

    a2 = TreeNode(4)
    b2 = TreeNode(5)
    c2 = TreeNode(6)
    d2 = TreeNode(7)
    e2 = TreeNode(2, a2, b2)
    f2 = TreeNode(3, c2, d2)
    r2 = TreeNode(1, e2, f2)

    a3 = TreeNode(4)
    b3 = TreeNode(6)
    c3 = TreeNode(5)
    d3 = TreeNode(7)
    e3 = TreeNode(2, a3, b3)
    f3 = TreeNode(3, c3, d3)
    r3 = TreeNode(1, e3, f3)

    print(verticalTraversal(r1))
    print(verticalTraversal(r2))
    print(verticalTraversal(r3))

