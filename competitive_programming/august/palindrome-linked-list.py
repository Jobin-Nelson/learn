'''
Created Date: 2022-08-23
Qn: Given the head of a singly linked list, return true if it is a palindrome.
Link: https://leetcode.com/problems/palindrome-linked-list/
Notes:
- Two pointer (fast, slow), and reverse one half of the list
'''
from __future__ import annotations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(arr: list[int]) -> ListNode | None:
        root = None
        for val in arr[::-1]:
            root = ListNode(val, root)
        return root

    def display(self) -> None:
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        print(result)

def isPalindrome(head: ListNode | None) -> bool:
    if not head: return False
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        nex = slow.next
        slow.next = prev
        prev = slow
        slow = nex

    l, r = head, prev
    while r:
        if l.val != r.val: return False
        l = l.next
        r = r.next
    return True

if __name__ == '__main__':
    h1, h2 = ListNode.from_list([1, 2, 2, 1]), ListNode.from_list([1, 2])
    print(isPalindrome(h1))
    print(isPalindrome(h2))
