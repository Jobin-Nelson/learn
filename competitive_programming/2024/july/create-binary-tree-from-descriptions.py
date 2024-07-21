"""
Created Date: 2024-07-15
Qn: You are given a 2D integer array descriptions where descriptions[i] =
    [parenti, childi, isLefti] indicates that parenti is the parent of childi
    in a binary tree of unique values. Furthermore,

    - If isLefti == 1, then childi is the left child of parenti. 
    - If isLefti == 0, then childi is the right child of parenti. Construct the
      binary tree described by descriptions and return its root.

    The test cases will be generated such that the binary tree is valid.
Link: https://leetcode.com/problems/create-binary-tree-from-descriptions/
Notes:
    - use graph and queue to construct Tree
"""
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        def inner(i: int) -> Self|None:
            if i >= len(arr) or arr[i] is None:
                return
            node = cls(arr[i])
            node.left = inner(i*2 + 1)
            node.left = inner(i*2 + 2)
            return node

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)
        
def createBinaryTree(descriptions: list[list[int]]) -> TreeNode|None:
    graph = {}
    roots = { d[0] for d in descriptions }
    for parent, child, is_left in descriptions:
        if parent not in graph:
            graph[parent] = [None,None]
        graph[parent][is_left ^ 1] = child
        roots.discard(child)
    root = TreeNode(roots.pop())
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val not in graph: continue
        left, right = graph[node.val]
        if left:
            node.left = TreeNode(left)
            q.append(node.left)
        if right:
            node.right = TreeNode(right)
            q.append(node.right)
    return root

if __name__ == '__main__':
    d1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    d2 = [[1,2,1],[2,3,0],[3,4,1]]


    print(createBinaryTree(d1))
    print(createBinaryTree(d2))
