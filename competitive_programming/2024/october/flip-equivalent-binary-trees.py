"""
Created Date: 2024-10-24
Qn: For a binary tree T, we can define a flip operation as follows: choose any
    node, and swap the left and right child subtrees.

    A binary tree X is flip equivalent to a binary tree Y if and only if we can
    make X equal to Y after some number of flip operations.

    Given the roots of two binary trees root1 and root2, return true if the two
    trees are flip equivalent or false otherwise.
Link: https://leetcode.com/problems/flip-equivalent-binary-trees/
Notes:
    - canonicalize both trees and compare recursively
"""

from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        def inner(i: int) -> Self | None:
            if i >= len(arr) or arr[i] is None:
                return
            node = cls(arr[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node

        return inner(0)

    def __str__(self) -> str:
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()


def flipEquiv(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def canonicalize(node: TreeNode | None) -> None:
        if node is None:
            return
        canonicalize(node.left)
        canonicalize(node.right)

        if node.right is None:
            return
        if node.left is None:
            node.left = node.right
            node.right = None
            return
        left = node.left
        right = node.right
        if left.val > right.val:
            node.left, node.right = node.right, node.left
        return

    def are_equivalent(node1: TreeNode | None, node2: TreeNode | None) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return are_equivalent(node1.left, node2.left) and are_equivalent(
            node1.right, node2.right
        )

    canonicalize(root1)
    canonicalize(root2)
    return are_equivalent(root1, root2)


if __name__ == '__main__':
    r11, r12 = (
        TreeNode.from_list([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
        TreeNode.from_list(
            [1, 3, 2, None, 6, 4, 5, None, None, None, None, None, None, 8, 7]
        ),
    )
    r21, r22 = TreeNode.from_list([]), TreeNode.from_list([])
    r31, r32 = TreeNode.from_list([]), TreeNode.from_list([1])
    r41, r42 = TreeNode.from_list([1, 2, 3]), TreeNode.from_list([1, 2, None, 3])
    r51, r52 = (
        TreeNode.from_list([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
        TreeNode.from_list([99, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]),
    )

    print(flipEquiv(r11, r12))
    print(flipEquiv(r21, r22))
    print(flipEquiv(r31, r32))
    print(flipEquiv(r41, r42))
