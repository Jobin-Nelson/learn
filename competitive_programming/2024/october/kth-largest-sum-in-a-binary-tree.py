"""
Created Date: 2024-10-22
Qn: You are given the root of a binary tree and a positive integer k.

    The level sum in the tree is the sum of the values of the nodes that are on
    the same level.

    Return the kth largest level sum in the tree (not necessarily distinct). If
    there are fewer than k levels in the tree, return -1.

    Note that two nodes are on the same level if they have the same distance
    from the root.
Link: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
Notes:
"""

from typing import Self
from collections import deque
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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

    def __repr__(self) -> str:
        return self.__str__()


def kthLargestLevelSum(root: TreeNode | None, k: int) -> int:
    if root is None:
        return -1
    heap = []
    q = deque([root])
    while q:
        level_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        heapq.heappush(heap, level_sum)
        if len(heap) > k:
            heapq.heappop(heap)
    if len(heap) < k:
        return -1
    print(heap)
    return heap[0]

    # if root is None:
    #     return -1
    # res = []
    #
    # def level_sum(node: TreeNode, level: int) -> None:
    #     nonlocal res
    #     if len(res) <= level:
    #         res.append(0)
    #     res[level] += node.val
    #     if node.left:
    #         level_sum(node.left, level + 1)
    #     if node.right:
    #         level_sum(node.right, level + 1)
    #
    # level_sum(root, 0)
    # sorted_sum_level = sorted(res, reverse=True)
    # return sorted_sum_level[k-1] if k < len(sorted_sum_level) else -1


if __name__ == '__main__':
    r1, k1 = TreeNode.from_list([5, 8, 9, 2, 1, 3, 7, 4, 6]), 2
    r2, k2 = TreeNode.from_list([1, 2, None, 3]), 1

    print(kthLargestLevelSum(r1, k1))
    print(kthLargestLevelSum(r2, k2))
