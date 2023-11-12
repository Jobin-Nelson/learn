"""
Created Date: 2023-03-16
Qn: Given two integer arrays inorder and postorder where inorder is the inorder
    traversal of a binary tree and postorder is the postorder traversal of the
    same tree, construct and return the binary tree.
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
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
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)

        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None:
                return None
            node = cls(arr[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node

        return inner(0)

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return str(res)


def buildTree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    if not inorder or not postorder:
        return None

    ip = len(inorder) - 1
    pp = len(postorder) - 1

    root = TreeNode(postorder[pp])
    st = [root]
    prev = None
    pp -= 1

    while pp >= 0:
        while st and st[-1].val == inorder[ip]:
            prev = st.pop()
            ip -= 1

        node = TreeNode(postorder[pp])

        if prev:
            prev.left = node
        elif st:
            curr_top = st[-1]
            curr_top.right = node

        st.append(node)
        prev = None
        pp -= 1

    return root


if __name__ == "__main__":
    i1, p1 = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    i2, p2 = [-1], [-1]

    print(buildTree(i1, p1))
    print(buildTree(i2, p2))
