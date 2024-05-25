"""
Created Date: 2024-05-17
Qn: Given a binary tree root and an integer target, delete all the leaf nodes
    with value target.

    Note that once you delete a leaf node with value target, if its parent node
    becomes a leaf node and has the value target, it should also be deleted
    (you need to continue doing that until you cannot).
Link: https://leetcode.com/problems/delete-leaves-with-a-given-value/
Notes:
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
            if i >= len(arr) or arr[i] is None:
                return None
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
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

def removeLeafNodes(root: TreeNode|None, target: int) -> TreeNode|None:
    if root is None: return None
    # BFS
    stack = [root]
    visited = set()
    parents = {root: None}

    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            if node.val == target:
                p = parents[node]
                if not p: return None
                if p.left == node: p.left = None
                if p.right == node: p.right = None
        elif node not in visited:
            visited.add(node)
            stack.append(node)
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
    return root


    # DFS (postorder)
    # def dfs(node: TreeNode) -> TreeNode|None:
    #     if node.left: node.left = dfs(node.left)
    #     if node.right: node.right = dfs(node.right)
    #     if node.left is None and node.right is None and node.val == target:
    #         return None
    #     return node
    # return dfs(root)

if __name__ == '__main__':
    r1, t1 = TreeNode.from_list([1,2,3,2,None,2,4]), 2
    r2, t2 = TreeNode.from_list([1,3,3,3,2]), 3
    r3, t3 = TreeNode.from_list([1,2,None,2,None,2]), 2

    print(removeLeafNodes(r1, t1))
    print(removeLeafNodes(r2, t2))
    print(removeLeafNodes(r3, t3))

