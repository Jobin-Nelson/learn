'''
Created Date: 2023-05-16
Qn: Given a linked list, swap every two adjacent nodes and return its head. You
    must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)
Link: https://leetcode.com/problems/swap-nodes-in-pairs/
Notes:
    - create dummy node
'''
from typing import Self
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        if not arr: return None
        head = cls()
        node = head.next = cls(arr[0])
        for i in range(1, len(arr)):
            node.next = cls(arr[i])
            node = node.next
        return head.next
    
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
        return str(res)

def swapPairs(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(0, head)
    prev, cur = dummy, head
    while cur and cur.next:
        # save nodes
        next_node = cur.next.next
        second_node = cur.next

        # reverse the nodes
        second_node.next = cur
        cur.next = next_node
        prev.next = second_node

        # update nodes
        prev = cur
        cur = next_node
    return dummy.next

if __name__ == '__main__':
    h1 = ListNode.from_list([1,2,3,4])
    h2 = ListNode.from_list([])
    h3 = ListNode.from_list([1])

    print(swapPairs(h1))
    print(swapPairs(h2))
    print(swapPairs(h3))
