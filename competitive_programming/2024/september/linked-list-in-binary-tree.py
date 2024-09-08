"""
Created Date: 2024-09-07
Qn: Given a binary tree root and a linked list with head as the first node. 

    Return True if all the elements in the linked list starting from the head
    correspond to some downward path connected in the binary tree otherwise
    return False.

    In this context downward path means a path that starts at some node and
    goes downwards.
Link: https://leetcode.com/problems/linked-list-in-binary-tree/
Notes:
    - use dfs
"""

from collections import deque
from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        cur = dummy = cls()
        for i in arr:
            cur.next = cls(i)
            cur = cur.next
        return dummy.next

    def __repr__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __str__(self) -> str:
        return self.__repr__()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)

        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None:
                return None
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
            return node

        return inner(0)

    def __repr__(self) -> str:
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

    def __str__(self) -> str:
        return self.__repr__()


def isSubPath(head: ListNode | None, root: TreeNode | None) -> bool:
    def dfs(list_node: ListNode | None, tree_node: TreeNode | None) -> bool:
        if list_node is None:
            return True
        if tree_node is None or list_node.val != tree_node.val:
            return False
        return dfs(list_node.next, tree_node.left) or dfs(
            list_node.next, tree_node.right
        )

    def check(head: ListNode | None, root: TreeNode | None) -> bool:
        if not root:
            return False
        return dfs(head, root) or check(head, root.left) or check(head, root.right)

    return check(head, root)


if __name__ == '__main__':
    h1, r1 = ListNode.from_list([4, 2, 8]), TreeNode.from_list(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    h2, r2 = ListNode.from_list([1, 4, 2, 6]), TreeNode.from_list(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )
    h3, r3 = ListNode.from_list([1, 4, 2, 6, 8]), TreeNode.from_list(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )

    print(isSubPath(h1, r1))
    print(isSubPath(h2, r2))
    print(isSubPath(h3, r3))
