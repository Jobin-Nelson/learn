"""
Created Date: 2024-03-12
Qn: Given the head of a linked list, we repeatedly delete consecutive sequences
    of nodes that sum to 0 until there are no such sequences.

    After doing so, return the head of the final linked list.  You may return
    any such answer.

    (Note that in the examples below, all sequences are serializations of
    ListNode objects.)
Link: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
Notes:
    - use dummy node in front
    - use prefix sum and hashtable to store the prefix sums with the node
    - couple the nodes having same prefix sums thus deleting nodes that add upto 0
"""
from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        cur = dummy = cls(0)
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return dummy.next

    def __str__(self) -> str:
        cur = self
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def removeZeroSumSublists(head: ListNode|None) -> ListNode|None:
    current = dummy = ListNode(0, head)

    prefix_sum = 0
    prefix_sum_to_node = {0: dummy}

    while current is not None:
        prefix_sum += current.val
        prefix_sum_to_node[prefix_sum] = current
        current = current.next

    prefix_sum = 0
    current = dummy

    while current is not None:
        prefix_sum += current.val
        current.next = prefix_sum_to_node[prefix_sum].next
        current = current.next
    return dummy.next

if __name__ == '__main__':
    h1 = ListNode.from_list([1,2,-3,3,1])
    h2 = ListNode.from_list([1,2,3,-3,4])
    h3 = ListNode.from_list([1,2,3,-3,-2])
    h4 = ListNode.from_list([5,-3,-4,1,6,-2,5])

    print(removeZeroSumSublists(h1))
    print(removeZeroSumSublists(h2))
    print(removeZeroSumSublists(h3))
