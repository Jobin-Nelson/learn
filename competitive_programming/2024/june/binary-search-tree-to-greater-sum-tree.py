"""
Created Date: 2024-06-25
Qn: Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
    such that every key of the original BST is changed to the original key plus
    the sum of all keys greater than the original key in BST.

    As a reminder, a binary search tree is a tree that satisfies these
    constraints:

        - The left subtree of a node contains only nodes with keys less than
          the node's key. 
        - The right subtree of a node contains only nodes with keys greater
          than the node's key. 
        - Both the left and right subtrees must also be binary search trees.

Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
Notes:
    - use reverse inorder traversal with nonlocal variable keeping track of cur
      sum
"""
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self|None:
        N = len(arr)
        def inner(i: int) -> Self|None:
            if i >= N or arr[i] is None: return
            node = cls(arr[i])
            node.left = inner(i*2 + 1)
            node.right = inner(i*2 + 2)
            return node
        return inner(0)

    def __str__(self) -> str:
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def bstToGst(root: TreeNode) -> TreeNode:
    cur_sum = 0
    def dfs(node: TreeNode|None):
        if not node: return
        nonlocal cur_sum
        dfs(node.right)
        tmp = node.val
        node.val += cur_sum
        cur_sum += tmp
        dfs(node.left)
    dfs(root)
    return root

if __name__ == '__main__':
    r1 = TreeNode.from_list([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    r2 = TreeNode.from_list([0,None,1])

    print(bstToGst(r1))
    print(bstToGst(r2))
