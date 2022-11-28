'''
Created Date: 06-06-2022
Qn: Given the heads of two singly linked-lists headA and headB, 
    return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Notes:
    - Traverse through the linked lists once list ends 
    - Begin from the other lists beginning
    - They should coincide at an intersection or none at the end of lists
'''
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1

if __name__ == '__main__':
    a1, a2 = ListNode(4), ListNode(1)
    b1, b2, b3 = ListNode(5), ListNode(6), ListNode(1)
    c1, c2, c3 = ListNode(8), ListNode(4), ListNode(5)
    a1.next = a2
    b1.next = b2
    b2.next = b3
    b3.next = c1
    a2.next = c1
    c1.next = c2
    c2.next = c3
    print(getIntersectionNode(a1, b1).val)
