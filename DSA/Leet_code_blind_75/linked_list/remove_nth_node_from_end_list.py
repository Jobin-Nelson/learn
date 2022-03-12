'''
Qn: Given the head of a linked list remove the nth node from the end of the list and return its head
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Notes:
- two pointer with n+1 gap between them, to get the node just before the node that needs to be deleted
'''
def remove_nth_from_end(head):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
