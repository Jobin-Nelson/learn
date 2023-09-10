'''
Created Date: 2023-09-04
Qn: Given head, the head of a linked list, determine if the linked list has a
    cycle in it.

    There is a cycle in a linked list if there is some node in the list that
    can be reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next
    pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return
    false.
Link: https://leetcode.com/problems/linked-list-cycle/
Notes:
'''
from typing import Self

class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        node = head = cls()

        for n in arr:
            node.next = cls(n)
            node = node.next
        return head.next
    
    def __str__(self) -> str:
        res, cur = [], self

        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

    def make_cycle(self, i: int) -> None:
        cur = head = self
        while cur.next:
            cur = cur.next
        for _ in range(i):
            head = head.next
        cur.next = head

def hasCycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

if __name__ == '__main__':
    h1 = ListNode.from_list([3,2,0,-4])
    h1.make_cycle(1)
    h2 = ListNode.from_list([1,2])
    h2.make_cycle(0)
    h3 = ListNode.from_list([1])

    print(hasCycle(h1))
    print(hasCycle(h2))
    print(hasCycle(h3))
