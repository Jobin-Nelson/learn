'''
Qn: Given head, the head of a linked list, determine if the linked list has a cycle in it.
Link: https://leetcode.com/problems/linked-list-cycle/
Notes:
- Tortoise and hare algorithm
- track two points one going slow traversing by one and other going fast traversing by two
- they are bound to meet each other if the linked list has a cycle and in linear time
'''
def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
