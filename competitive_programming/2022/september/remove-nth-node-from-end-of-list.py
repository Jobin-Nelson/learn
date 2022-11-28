'''
Created Date: 2022-09-28
Qn: Given the head of a linked list, remove the nth node from the end of the
    list and return its head.
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Notes:
    - two pointer, iterate to the end of list
    - skip the next for left pointer
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    l, r = dummy, head

    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next
    return dummy.next

if __name__ == '__main__':
    a1 = ListNode(5)
    b1 = ListNode(4, a1)
    c1 = ListNode(3, b1)
    d1 = ListNode(2, c1)
    h1 = ListNode(1, d1)
    n1 = 2

    h2 = ListNode(1)
    n2 = 1

    a3 = ListNode(2)
    h3 = ListNode(1, a3)
    n3 = 1

    print(removeNthFromEnd(h1, n1))
    print(removeNthFromEnd(h2, n2))
    print(removeNthFromEnd(h3, n3))
