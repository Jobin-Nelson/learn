'''
Created Date: 2022-12-06
Qn: Given the head of a singly linked list, group all the nodes with odd
    indices together followed by the nodes with even indices, and return the
    reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should
    remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time
    complexity.
Link: https://leetcode.com/problems/odd-even-linked-list/
Notes:
    - create 2 new ListNode for even_head and odd_head
    - string them accordingly as you go through the nodes
    - attach even_head to odd_node.next
    - close the even_node.next = None
    - return odd_head.next
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def oddEvenList(head: ListNode | None) -> ListNode | None:
    odd_head = ListNode()
    even_head = ListNode()
    odd_node = odd_head
    even_node = even_head
    is_even = False

    while head:
        if is_even:
            is_even = False
            even_node.next = head
            even_node = even_node.next
        else:
            is_even = True
            odd_node.next = head
            odd_node = odd_node.next
        head = head.next
    odd_node.next = even_head.next
    even_node.next = None
    return odd_head.next

if __name__ == '__main__':
    a1 = ListNode(5)
    b1 = ListNode(4, a1)
    c1 = ListNode(3, b1)
    d1 = ListNode(2, c1)
    h1 = ListNode(1, d1)

    a2 = ListNode(7)
    b2 = ListNode(4, a2)
    c2 = ListNode(6, b2)
    d2 = ListNode(5, c2)
    e2 = ListNode(3, d2)
    f2 = ListNode(1, e2)
    h2 = ListNode(2, f2)

    print(oddEvenList(h1))
    print(oddEvenList(h2))
