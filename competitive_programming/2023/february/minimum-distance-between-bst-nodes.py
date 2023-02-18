'''
Created Date: 2023-02-17
Qn: Given the root of a Binary Search Tree (BST), return the minimum difference
    between the values of any two different nodes in the tree.
Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
Notes:
    - use inorder traversal dfs
    - at any point in traversal you check min between cur node val and previous node val
'''
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)

        def inner(index: int) -> Self | None:
            if index >= N or arr[index] is None: return

            node = cls(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return inner(0)

    def __str__(self):
        q = deque([self])
        res = []

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def minDiffInBST(root: TreeNode | None):
    prev = None
    res = float('inf')
    def inOrder(node: TreeNode | None):
        nonlocal res, prev
        if not node: return
        inOrder(node.left)
        if prev: res = min(res, node.val - prev.val)
        prev = node
        inOrder(node.right)
    inOrder(root)
    return res

if __name__ == '__main__':
    r1 = [4,2,6,1,3]
    r2 = [1,0,48,None,None,12,49]

    print(minDiffInBST(TreeNode.from_list(r1)))
    print(minDiffInBST(TreeNode.from_list(r2)))
