'''
Qn: Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Notes:
- use level order traversal to link each node to the next one
- can be done using only constant space
'''
from __future__ import annotations
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Node) -> Node:
    if not root: return
    q = deque()
    q.append(root)
    while q:
        pre = None
        for _ in range(len(q)):
            cur = q.popleft()
            if pre: pre.next = cur
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
            pre = cur
    return root

def connect_no_extra_space(root: Node) -> Node:
    leftmost = root
    while leftmost:
        cur = leftmost
        leftmost = pre = None
        while cur:
            if cur.left: 
                if not leftmost: leftmost = cur.left
                if pre: pre.next = cur.left
                pre = cur.left
            if cur.right: 
                if not leftmost: leftmost = cur.right
                if pre: pre.next = cur.right
                pre = cur.right
            cur = cur.next
    return root

def print_binary(root: Node):
    if not root: return []
    q = deque()
    q.append(root)
    res = []
    while q:
        level = []
        q_len = len(q)
        for _ in range(q_len):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left: 
                q.append(cur.left)
            if cur.right: 
                q.append(cur.right)
            if cur.next is None: level.append('#')
        if level: res.extend(level)
    return res

if __name__ == '__main__':
    a = Node(1)
    b, c = Node(2), Node(3)
    d, e, f = Node(4), Node(5), Node(7)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f

    #connect(a)
    connect_no_extra_space(a)
    print(print_binary(a))
