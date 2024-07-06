"""
Created Date: 2024-07-05
Qn: A critical point in a linked list is defined as either a local maxima or a
    local minima.

    A node is a local maxima if the current node has a value strictly greater
    than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller
    than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a
    previous node and a next node.

    Given a linked list head, return an array of length 2 containing
    [minDistance, maxDistance] where minDistance is the minimum distance
    between any two distinct critical points and maxDistance is the maximum
    distance between any two distinct critical points. If there are fewer than
    two critical points, return [-1, -1].
Link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
Notes:
    - one pass
"""
from typing import Self
from sys import maxsize


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        dummy = cur = cls()
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

def nodesBetweenCriticalPoints(head: ListNode|None) -> list[int]:
    cur = head
    prev1 = prev2 = None
    while prev1 is None:
        if cur is None:
            return [-1, -1]
        prev1 = prev2
        prev2 = cur.val
        cur = cur.next

    index = 2
    first_critical = 0
    last_critical = 0
    criticals = 0

    min_distance = maxsize
    while cur:
        if (prev1 < prev2 and prev2 > cur.val) or (prev1 > prev2 and prev2 < cur.val):
            if first_critical == 0:
                first_critical = index
            if last_critical != 0:
                min_distance = min(min_distance, index - last_critical)
            last_critical = index
            criticals += 1
        index += 1
        prev1 = prev2
        prev2 = cur.val
        cur = cur.next

    if criticals < 2:
        return [-1, -1]
    return [min_distance, last_critical - first_critical]
    # if len(criticals) < 2:
    #     return [-1, -1]
    # min_distance = maxsize
    # max_distance = criticals[-1] - criticals[0]
    # for i in range(len(criticals)-1):
    #     min_distance = min(min_distance, criticals[i+1] - criticals[i])
    # return [min_distance, max_distance]


if __name__ == '__main__':
    h1 = ListNode.from_list([3,1])
    h2 = ListNode.from_list([5,3,1,2,5,1,2])
    h3 = ListNode.from_list([1,3,2,2,3,2,2,2,7])

    print(nodesBetweenCriticalPoints(h1))
    print(nodesBetweenCriticalPoints(h2))
    print(nodesBetweenCriticalPoints(h3))
