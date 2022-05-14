'''
Qn: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Notes:
- define a function to merge two lists at a time
- iterate over the lists with step 2 till length of lists is 1
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def merge_k_lists(self, lists: list[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge(list1, list2))
            lists = merged_lists
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next

def print_linked_list_rec(head):
    if head == None:
        return None
    print(head.val, end='->')
    print_linked_list_rec(head.next)

if __name__ == '__main__':
    l11 = ListNode(5)
    l12 = ListNode(4, l11)
    l13 = ListNode(1, l12)
    l14 = ListNode(4)
    l15 = ListNode(3, l14)
    l16 = ListNode(1, l15)
    l17 = ListNode(6)
    l18 = ListNode(2, l17)
    l1 = [l13, l16, l18]
    l2 = []
    s = Solution()
    print_linked_list_rec(s.merge_k_lists(l1))
    print_linked_list_rec(s.merge_k_lists(l2))
