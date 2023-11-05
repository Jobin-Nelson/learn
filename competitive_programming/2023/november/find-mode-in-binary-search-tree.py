'''
Created Date: 2023-11-01
Qn: Given the root of a binary search tree (BST) with duplicates, return all
    the mode(s) (i.e., the most frequently occurred element) in it.

    If the tree has more than one mode, return them in any order.

    Assume a BST is defined as follows:

        - The left subtree of a node contains only nodes with keys less than or
          equal to the node's key. 
        - The right subtree of a node contains only nodes with keys greater
          than or equal to the node's key. 
        - Both the left and right subtrees must also be binary search trees.

Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
Notes:
    - use dfs, bfs, inorder and morris (space complexity O(1)) traversal 
'''
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        if not arr: return None
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
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
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def findMode(root: TreeNode | None) -> list[int]:
    # morris traversal
    if root is None: return []
    cur_num = cur_streak = max_streak = 0
    res = []
    cur = root
    while cur:
        if cur.left:
            friend = cur.left
            while friend.right:
                friend = friend.right
            friend.right = cur
            left = cur.left
            cur.left = None
            cur = left
        else:
            num = cur.val
            if num == cur_num:
                cur_streak += 1
            else:
                cur_streak = 1
                cur_num = num
            if cur_streak > max_streak:
                res = []
                max_streak = cur_streak
            if cur_streak == max_streak:
                res.append(num)
            cur = cur.right
    return res

    # Inorder traversal
    # if root is None: return []
    # cur_num = cur_streak = max_streak = 0
    # res = []
    # def dfs(node: TreeNode):
    #     nonlocal cur_num, cur_streak, max_streak, res
    #     if node.left: dfs(node.left)
    #     num = node.val
    #     if num == cur_num:
    #         cur_streak += 1
    #     else:
    #         cur_streak = 1
    #         cur_num = num
    #     if cur_streak > max_streak:
    #         res = []
    #         max_streak = cur_streak
    #     if cur_streak == max_streak:
    #         res.append(num)
    #     if node.right: dfs(node.right)
    # dfs(root)
    #
    # return res

    # bfs
    # if root is None: return []
    # count = {}
    # q = deque([root])
    # while q:
    #     node = q.popleft()
    #     count[node.val] = count.get(node.val, 0) + 1
    #     if node.left: q.append(node.left)
    #     if node.right: q.append(node.right)
    #
    # max_count = max(count.values())
    # return [k for k,v in count.items() if v == max_count]

if __name__ == '__main__':
    r1 = TreeNode.from_list([1, None, 2, 2])
    r2 = TreeNode.from_list([0])

    print(findMode(r1))
    print(findMode(r2))
