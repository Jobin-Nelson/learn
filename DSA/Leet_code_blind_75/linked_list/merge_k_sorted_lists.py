'''
Qn: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Notes:
- use merge sort algorithm till the length of list is 1
- use merge two linked lists as helper function to take care of two linked lists at a time
'''

def merge_k_lists(lists):
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        merged_list = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 <= len(lists) else None
            merged_list.append(merge(l1, l2))
        lists = merged_list
    return lists[0]

def merge(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1.val
            l1 = l1.next
        else:
            tail.next = l2.val
            l2 = l2.next
        tail = tail.next
    if l1: tail.next = l1
    if l2: tail.next = l2
    return dummy.next