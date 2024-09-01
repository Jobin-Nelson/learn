"""
Created Date: 2024-08-26
Qn: Given the root of an n-ary tree, return the postorder traversal of its
    nodes' values.

    Nary-Tree input serialization is represented in their level order
    traversal. Each group of children is separated by the null value (See
    examples)
Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Notes:
    - use dfs
"""

from collections import deque
from typing import Self


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        if not arr:
            return None
        root = cls(arr[0])
        if len(arr) <= 3:
            return root
        q = deque([root])
        i = 2
        while q and i < len(arr):
            node = q.popleft()
            cur_children = []
            while i < len(arr) and arr[i] is not None:
                child = cls(arr[i])
                cur_children.append(child)
                q.append(child)
                i += 1
            if cur_children:
                node.children = cur_children
            i += 1
        return root

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.children:
                    for n in node.children:
                        q.append(n)
            res.append(None)
        return str(res)


def postOrder(root: Node | None) -> list[int]:
    # Iterative approach
    if root is None:
        return []
    stack = [(root, False)]
    res = []

    while stack:
        node, visited = stack.pop()
        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))
            for c in node.children[::-1]:
                stack.append((c, False))
    return res


    # Recursive approach
    # if root is None:
    #     return []
    # res = []
    #
    # def dfs(node: Node):
    #     if node.children is None:
    #         return
    #     for n in node.children:
    #         dfs(n)
    #     res.append(node.val)
    #
    # dfs(root)
    # return res


if __name__ == '__main__':
    r1 = Node.from_list([1, None, 3, 2, 4, None, 5, 6])
    r2 = Node.from_list(
        [
            1,
            None,
            2,
            3,
            4,
            5,
            None,
            None,
            6,
            7,
            None,
            8,
            None,
            9,
            10,
            None,
            None,
            11,
            None,
            12,
            None,
            13,
            None,
            None,
            14,
        ]
    )

    print(postOrder(r1))
    print(postOrder(r2))
