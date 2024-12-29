"""
Created Date: 2024-12-23
Qn: You are given the root of a binary tree with unique values.

    In one operation, you can choose any two nodes at the same level and swap
    their values.

    Return the minimum number of operations needed to make the values at each
    level sorted in a strictly increasing order.

    The level of a node is the number of edges along the path between it and
    the root node.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
Notes:
"""

from typing import Self
from collections import deque
import unittest


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


class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        res = 0
        q = deque([root])
        mask = 0xFFFFF
        shift = 20
        while q:
            nodes = []
            for i in range(len(q)):
                node = q.popleft()
                nodes.append((node.val << shift) + i)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # bit manipulation
            nodes.sort()
            swaps = 0
            i = 0
            while i < len(nodes):
                orig_pos = nodes[i] & mask
                if orig_pos != i:
                    nodes[i], nodes[orig_pos] = nodes[orig_pos], nodes[i]
                    swaps += 1
                    i -= 1
                i += 1
            res += swaps
        return res

            # use hashmap and count the swaps needed
            # mapIndex = {n: i for i, n in enumerate(nodes)}
            # swaps = 0
            # sorted_nodes = sorted(nodes)
            # for i in range(len(nodes)):
            #     if nodes[i] != sorted_nodes[i]:
            #         swaps += 1
            #     j = mapIndex[sorted_nodes[i]]
            #     nodes[i], nodes[j] = nodes[j], nodes[i]
            #     mapIndex[nodes[i]] = i
            #     mapIndex[nodes[j]] = j
            # res += swaps
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumOperations1(self):
        r = TreeNode.from_list(
            [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
        )
        expected = 3
        self.assertEqual(expected, self.sol.minimumOperations(r))

    def test_minimumOperations2(self):
        r = TreeNode.from_list([1, 3, 2, 7, 6, 5, 4])
        expected = 3
        self.assertEqual(expected, self.sol.minimumOperations(r))

    def test_minimumOperations3(self):
        r = TreeNode.from_list(list(range(1, 7)))
        expected = 0
        self.assertEqual(expected, self.sol.minimumOperations(r))


if __name__ == '__main__':
    unittest.main()
