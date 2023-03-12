'''
Created Date: 2023-03-11
Qn: Given the head of a singly linked list where elements are sorted in
    ascending order, convert it to a height-balanced binary search tree.
Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Notes:
    - find the middle, detach slow pointer
    - recursively update left tree with left linked list and right tree with
      right linked list
'''
from typing import Self
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)
        def dfs(i: int) -> Self | None:
            if i >= N: return None
            node = cls(arr[i])
            node.next = dfs(i+1)
            return node
        return dfs(0)
    
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N: return None
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

class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head: return None
        if not head.next: return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.next.val)
        right_head = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_head)
        return root

if __name__ == '__main__':
    h1 = ListNode.from_list([-10,-3,0,5,9])
    h2 = ListNode.from_list([])

    s = Solution()
    print(s.sortedListToBST(h1))
    print(s.sortedListToBST(h2))
