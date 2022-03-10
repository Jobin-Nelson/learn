'''
Qn: Given the head of a singly linked list, reverse the list, and return the reversed list.
Link: https://leetcode.com/problems/reverse-linked-list/
Notes:
- track previous, current, next and update them by rewiring the next with the previous as you traverse the linked list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_list(head):
    pre = None
    while head:
        nex = head.next
        head.next = pre
        pre = head
        head = nex
    return pre
