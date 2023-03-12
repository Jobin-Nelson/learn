'''
Created Date: 2023-03-09
Qn: Given the head of a linked list, return the node where the cycle begins. If
    there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that
    can be reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next
    pointer is connected to (0-indexed). It is -1 if there is no cycle. Note
    that pos is not passed as a parameter.

    Do not modify the linked list.
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Notes:
    - use fast and slow to detect the cycle
    - reset slow to head and move both pointers by one node at a time to find
      the position of cycle
'''
from __future__ import annotations
from typing import Self

class ListNode:
    def __init__(self, x, next: ListNode | None = None):
        self.val = x
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        def dfs(i: int) -> Self | None:
            if i == len(arr): return None
            node = cls(arr[i])
            node.next = dfs(i + 1)
            return node
        return dfs(0)

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def detectCycle(head: ListNode | None) -> ListNode | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

if __name__ == '__main__':
    h1 = ListNode.from_list([3,2,0,-4])
    h2 = ListNode.from_list([1,2])
    h3 = ListNode.from_list([1])

    print(detectCycle(h1))
    print(detectCycle(h2))
    print(detectCycle(h3))
