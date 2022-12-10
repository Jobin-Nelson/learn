'''
Created Date: 2022-12-05
Qn: Given the head of a singly linked list, return the middle node of the
    linked list.

    If there are two middle nodes, return the second middle node.
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Notes:
    - fast and slow pointers
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def middleNode(head: ListNode | None) -> ListNode | None:
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    a1 = ListNode(5)
    b1 = ListNode(4, a1)
    c1 = ListNode(3, b1)
    d1 = ListNode(2, c1)
    h1 = ListNode(1, d1)

    e2 = ListNode(6)
    a2 = ListNode(5, e2)
    b2 = ListNode(4, a2)
    c2 = ListNode(3, b2)
    d2 = ListNode(2, c2)
    h2 = ListNode(1, d2)

    print(middleNode(h1))
    print(middleNode(h2))
