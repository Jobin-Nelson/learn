'''
Created Date: 2022-10-13
Qn: There is a singly-linked list head and we want to delete a node node in it.

    You are given the node to be deleted node. You will not be given access to
    the first node of head.

    All the values of the linked list are unique, and it is guaranteed that the
    given node node is not the last node in the linked list.

    Delete the given node. Note that by deleting the node, we do not mean
    removing it from memory. We mean:

        - The value of the given node should not exist in the linked list. 
        - The number of nodes in the linked list should decrease by one. 
        - All the values before node should be in the same order. 
        - All the values after node should be in the same order. 

    Custom testing:

        - For the input, you should provide the entire linked list head and the
          node to be given node. node should not be the last node of the list
          and should be an actual node in the list. 
        - We will build the linked list and pass the node to your function. 
        - The output will be the entire list after calling your function.
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
Notes:
    - inplace deletion of node can be achieved by
    - replace the current value to the next node value
    - point next to the next of next node
'''
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next

if __name__ == '__main__':
    a1 = ListNode(9)
    b1 = ListNode(1, a1)
    c1 = ListNode(5, b1)
    h1 = ListNode(4, c1)
    deleteNode(c1)
    print(h1)

    a2 = ListNode(9)
    b2 = ListNode(1, a2)
    c2 = ListNode(5, b2)
    h2 = ListNode(4, c2)
    deleteNode(b2)
    print(h2)
