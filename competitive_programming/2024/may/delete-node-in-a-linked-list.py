"""
Created Date: 2024-05-05
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
"""
from typing import Self

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None
    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        dummy = cur = cls(0)
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return dummy.next
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)
    def __repr__(self) -> str:
        return self.__str__()
    def find_node(self, node: int) -> Self|None:
        cur = self
        while cur:
            if cur.val == node: return cur
            cur = cur.next

def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next
    # prev = cur = node
    # while cur.next:
    #     cur.val = cur.next.val
    #     prev = cur
    #     cur = cur.next
    # prev.next = None

if __name__ == '__main__':
    h1, n1 = ListNode.from_list([4,5,1,9]), 5
    h2, n2 = ListNode.from_list([4,5,1,9]), 1


    deleteNode(h1.find_node(n1))
    deleteNode(h2.find_node(n2))
    print(h1)
    print(h2)
