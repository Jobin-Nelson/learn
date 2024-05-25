"""
Created Date: 2024-05-16
Qn: You are given the root of a full binary tree with the following properties:

        - Leaf nodes have either the value 0 or 1, where 0 represents False and
          1 represents True. 
        - Non-leaf nodes have either the value 2 or 3, where 2 represents the
          boolean OR and 3 represents the boolean AND.

    The evaluation of a node is as follows:

        - If the node is a leaf node, the evaluation is the value of the node,
          i.e. True or False. 
        - Otherwise, evaluate the node's two children and apply the boolean
          operation of its value with the children's evaluations.

    Return the boolean result of evaluating the root node.

    A full binary tree is a binary tree where each node has either 0 or 2
    children.

    A leaf node is a node that has zero children.
Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/
Notes:
"""
from __future__ import annotations
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Self|None = None, right: Self|None = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self|None:
        N =  len(arr)
        def inner(i: int) -> Self|None:
            if i >= N or arr[i] is None:
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

def evaluateTree(root: TreeNode|None) -> bool:
    if root is None: return False
    def dfs(node: TreeNode) -> bool:
        if node.val == 3:
            return dfs(node.left) and dfs(node.right)
        elif node.val == 2:
            return dfs(node.left) or dfs(node.right)
        else:
            return bool(node.val)
    return dfs(root)

if __name__ == '__main__':
    r1 = TreeNode.from_list([2,1,3,None,None,0,1])
    r2 = TreeNode.from_list([0])

    print(evaluateTree(r1))
    print(evaluateTree(r2))
