'''
Created Date: 2023-05-17
Qn: In a linked list of size n, where n is even, the ith node (0-indexed) of
    the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n
    / 2) - 1.

        - For example, if n = 4, then node 0 is the twin of node 3, and node 1
          is the twin of node 2. These are the only nodes with twins for n = 4.

    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list with even length, return the maximum twin
    sum of the linked list.
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
Notes:
    - use fast and slow to find the mid node
    - and reverse the linked list of slow
    - iterate through the left and right half from the middle
'''
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)
        if not arr: return None
        head = cls()
        node = head.next = cls(arr[0])

        for i in range(1, N):
            node.next = cls(arr[i])
            node = node.next
        return head.next
    
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)
    
def pairSum(head: ListNode | None) -> int:
    slow, fast = head, head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        slow_next=  slow.next
        slow.next = prev
        prev = slow
        slow = slow_next

    res = 0
    while slow:
        res = max(res, prev.val + slow.val)
        prev = prev.next
        slow = slow.next
    return res

if __name__ == '__main__':
    h1 = ListNode.from_list([5,4,2,1])
    h2 = ListNode.from_list([4,2,2,3])
    h3 = ListNode.from_list([1,100000])

    print(pairSum(h1))
    print(pairSum(h2))
    print(pairSum(h3))
