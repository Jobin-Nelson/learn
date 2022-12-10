'''
Created Date: 2022-12-08
Qn: Consider all the leaves of a binary tree, from left to right order, the
    values of those leaves form a leaf value sequence.

    For example, in the given tree above, the leaf value sequence is 
    (6, 7, 4, 9, 8).

    Two binary trees are considered leaf-similar if their leaf value sequence
    is the same.

    Return true if and only if the two given trees with head nodes root1 and
    root2 are leaf-similar.
Link: https://leetcode.com/problems/leaf-similar-trees/
Notes:
    - use dfs
'''
from collections import deque
from typing import Iterator, Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)
        if N == 0: return None

        def inner(index: int = 0) -> Self | None:
            if index >= N or arr[index] is None:
                return None
            node = cls(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return inner()

    def __str__(self) -> str:
        cur = self
        q = deque([cur])
        res = []

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)


def leafSimilar(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    if not root1 or not root2: return False

    def leaf(node: TreeNode) -> Iterator[int]:
            if node.left or node.right:
                if node.left:
                    for key in leaf(node.left):
                        yield key
                if node.right:
                    for key in leaf(node.right):
                        yield key
            else:
                yield node.val

    return list(leaf(root1)) == list(leaf(root2))

    # def get_leaf(node: TreeNode | None, arr: list) -> list | None:
    #     if not node: return 
    #     if not node.left and not node.right: arr.append(node.val)
    #     get_leaf(node.left, arr)
    #     get_leaf(node.right, arr)
    #     return arr
    # return get_leaf(root1, []) == get_leaf(root2, [])

if __name__ == '__main__':
    r11 = TreeNode.from_list([3,5,1,6,2,9,8,None,None,7,4])
    r12 = TreeNode.from_list([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])

    r21 = TreeNode.from_list([1, 2, 3])
    r22 = TreeNode.from_list([1, 3, 2])

    print(leafSimilar(r11, r12))
    print(leafSimilar(r21, r22))
