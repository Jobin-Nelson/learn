'''
Created Date: 2023-02-28
Qn: Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node
    of any one of them.

    Two trees are duplicate if they have the same structure with the same node
    values.
Link: https://leetcode.com/problems/find-duplicate-subtrees/
Notes:
    - use hashmap to count the number of occurences of same tree
'''
from typing import Self
from collections import deque, Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)

        def inner(index: int) -> Self | None:
            if index >= N or arr[index] is None: return None
            node = cls(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
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

    def __repr__(self) -> str:
        res = []
        q = deque([self])

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def findDuplicateSubtrees(root: TreeNode | None) -> list[TreeNode | None]:
    res = []
    count = Counter()

    def encode(node: TreeNode | None) -> str:
        if not node: return ''
        encoded = str(node.val) + '#' + encode(node.left) + '#' + encode(node.right)
        count[encoded] += 1
        if count[encoded] == 2: res.append(node)
        return encoded
    encode(root)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,3,4,None,2,4,None,None,4])
    r2 = TreeNode.from_list([2,1,1])
    r3 = TreeNode.from_list([2,2,2,3,None,3,None])

    print(findDuplicateSubtrees(r1))
    print(findDuplicateSubtrees(r2))
    print(findDuplicateSubtrees(r3))
