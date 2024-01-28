"""
Created Date: 2024-01-24
Qn: Given a binary tree where node values are digits from 1 to 9. A path in the
    binary tree is said to be pseudo-palindromic if at least one permutation of
    the node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to
    leaf nodes.
Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
Notes:
    - Get the root to leaf path using iterative or recursive appraoch
    - since there is a constraint on the values [0-9]. We can use bitmask to
      count the frequency and ensure that we have atmost one odd frequency
"""
from collections import deque
from typing import Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self | None:
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(i*2+1)
            node.right = inner(i*2+2)
            return node
        return inner(0)

    def __str__(self) -> str:
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def pseudoPalindromicPaths(root: TreeNode | None) -> int:
    res = 0
    stack = [(root, 0)]
    while stack:
        node, path = stack.pop()
        if node is not None:
            path ^= (1 << node.val)
            if node.left is None and node.right is None:
                if path & (path - 1) == 0:
                    res += 1
            else:
                stack.append((node.left, path))
                stack.append((node.right, path))
    return res
    # dfs approach
    # if root is None: return 0
    # paths = []
    # def dfs(node: TreeNode, cur_path: list[int]) -> None:
    #     if node.left is None and node.right is None:
    #         paths.append(cur_path + [node.val])
    #         return
    #     if node.left: dfs(node.left, cur_path + [node.val])
    #     if node.right: dfs(node.right, cur_path + [node.val])
    # dfs(root, [])
    #
    # res = 0
    # for path in paths:
    #     counter = Counter(path)
    #     valid = True
    #     ones = 0
    #     for v in counter.values():
    #         if v == 1:
    #             if ones == 1:
    #                 valid = False
    #                 break
    #             ones += 1
    #         elif v > 2:
    #             valid = False
    #             break
    #     if valid: res += 1
    # return res


if __name__ == '__main__':
    r1 = TreeNode.from_list([2,3,1,3,1,None,1])
    r2 = TreeNode.from_list([2,1,1,1,3,None,None,None,None,None,1])
    r3 = TreeNode.from_list([9])
    r4 = TreeNode.from_list([9,5,4,5,None,2,6,2,5,None,8,3,9,2,3,1,1,None,4,5,4,2,2,6,4,None,None,1,7,None,5,4,7,None,None,7,None,1,5,6,1,None,None,None,None,9,2,None,9,7,2,1,None,None,None,6,None,None,None,None,None,None,None,None,None,5,None,None,3,None,None,None,8,None,1,None,None,8,None,None,None,None,2,None,8,7])

    print(pseudoPalindromicPaths(r1))
    print(pseudoPalindromicPaths(r2))
    print(pseudoPalindromicPaths(r3))
    print(pseudoPalindromicPaths(r4))
