"""
Created Date: 2024-03-22
Qn: Given the head of a singly linked list, return true if it is a
    palindrome or false otherwise.
Link: https://leetcode.com/problems/palindrome-linked-list/
Notes:
    - use fast and slow pointer
    - reverse the second half of the linked list and check palindrom from both ends
"""
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        cur = dummy = cls()
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return dummy.next

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def isPalindrome(head: ListNode|None) -> bool:
    fast = slow = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev: prev.next = None
    prev = None
    while slow:
        nex = slow.next
        slow.next = prev
        prev = slow
        slow = nex
    while head and prev and head.val == prev.val:
        head = head.next
        prev = prev.next
    return head is None and (prev is None or prev.next is None)

if __name__ == '__main__':
    h1 = ListNode.from_list([1,2,2,1])
    h2 = ListNode.from_list([1,2])

    print(isPalindrome(h1))
    print(isPalindrome(h2))
    
