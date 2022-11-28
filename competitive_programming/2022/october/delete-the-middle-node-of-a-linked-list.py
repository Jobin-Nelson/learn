'''
Created Date: 2022-10-14
Qn: You are given the head of a linked list. Delete the middle node, and return
    the head of the modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start
    using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or
    equal to x.

    - For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
    respectively.
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Notes:
    - Two pointer solution
    - one pointer travels twice as fast as the other
    - when the fastest pointer reaches the end the slow pointer should have
      reached the middle
    - we just keep a variable to track the previous slow pointer so that we can
      skip the next node which is the middle node
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

def deleteMiddle(head: ListNode | None) -> ListNode | None:
    slow, fast = head, head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if not prev: return None
    prev.next = slow.next
    return head

if __name__ == '__main__':
    a1 = ListNode(6)
    b1 = ListNode(2, a1)
    c1 = ListNode(1, b1)
    d1 = ListNode(7, c1)
    e1 = ListNode(4, d1)
    f1 = ListNode(3, e1)
    h1 = ListNode(1, f1)
    print(deleteMiddle(h1))

    a2 = ListNode(4)
    b2 = ListNode(3, a2)
    c2 = ListNode(2, b2)
    h2 = ListNode(1, c2)
    print(deleteMiddle(h2))
