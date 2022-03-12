''''
Qn: You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
Link: https://leetcode.com/problems/reorder-list/
Notes: 
- find the middle
- reverse the second half
- merge the two halves
'''
def reorder_list(head):
    slow, fast = head, head.next

    # finding the middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next

    # reverse the second half
    prev = slow.next = None
    while second:
        nex = second.next
        second.next = prev
        prev = second
        second = nex

    # merge the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
