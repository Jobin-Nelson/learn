"""
Created Date: 2024-07-17
Qn: Given the root of a binary tree, each node in the tree has a distinct
    value.

    After deleting all nodes with a value in to_delete, we are left with a
    forest (a disjoint union of trees).

    Return the roots of the trees in the remaining forest. You may return the
    result in any order.
Link: https://leetcode.com/problems/delete-nodes-and-return-forest/
Notes:
    - use dfs
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
        def inner(i: int) -> Self|None:
            if i >= len(arr) or arr[i] is None: return
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

    def __repr__(self) -> str:
        return self.__str__()

def delNodes(root: TreeNode|None, to_delete: list[int]) -> list[TreeNode]:
    if root is None: return []
    to_delete_set = set(to_delete)
    roots: set[TreeNode] = set([root])
    def dfs(node: TreeNode) -> bool:
        is_delete = False
        if node.val in to_delete_set:
            roots.discard(node)
            if node.left: roots.add(node.left)
            if node.right: roots.add(node.right)
            is_delete = True
        if node.left and dfs(node.left):
            node.left = None
        if node.right and dfs(node.right):
            node.right = None
        return is_delete
    dfs(root)
    return list(roots)

if __name__ == '__main__':
    r1, d1 = TreeNode.from_list([1,2,3,4,5,6,7]), [3,5]
    r2, d2 = TreeNode.from_list([1,2,4,None,3]), [3]

    print(delNodes(r1, d1))
    print(delNodes(r2, d2))
