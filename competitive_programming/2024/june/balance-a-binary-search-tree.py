"""
Created Date: 2024-06-26
Qn: Given the root of a binary search tree, return a balanced binary search
    tree with the same node values. If there is more than one answer, return
    any of them.

    A binary search tree is balanced if the depth of the two subtrees of every
    node never differs by more than 1.
Link: https://leetcode.com/problems/balance-a-binary-search-tree/
Notes:
    - use inorder traversal
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
            node.left = inner(i*2+1)
            node.right = inner(i*2+2)
            return node
        return inner(0)

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)


def balanceBST(root: TreeNode|None) -> TreeNode|None:
    def inorder_traversal(node: TreeNode|None, inorder: list[int]):
        if not node: return
        inorder_traversal(node.left, inorder)
        inorder.append(node.val)
        inorder_traversal(node.right, inorder)
    def create_balanced_bst(inorder: list[int], start: int, end: int) -> TreeNode|None:
        if start > end: return
        mid = start + ((end - start) >> 1)
        left_node = create_balanced_bst(inorder, start, mid-1)
        right_node = create_balanced_bst(inorder, mid+1, end)
        return TreeNode(inorder[mid], left_node, right_node)
    inorder = []
    inorder_traversal(root, inorder)
    return create_balanced_bst(inorder, 0, len(inorder)-1)


if __name__ == '__main__':
    r1 = TreeNode.from_list([1,None,2,None,None,None,3,None,None,None,None,None,4,None,None,None,None,None,None,None,None,None,None])
    r2 = TreeNode.from_list([2,1,3])

    print(balanceBST(r1))
    print(balanceBST(r1))
