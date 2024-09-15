"""
Created Date: 2024-09-09
Qn: You are given two integers m and n, which represent the dimensions of a
    matrix.

    You are also given the head of a linked list of integers.

    Generate an m x n matrix that contains the integers in the linked list
    presented in spiral order (clockwise), starting from the top-left of the
    matrix. If there are remaining empty spaces, fill them with -1.

    Return the generated matrix.
Link: https://leetcode.com/problems/spiral-matrix-iv/
Notes:
    - use directions to simulate spiraling
"""

from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        cur = dummy = cls()
        for i in arr:
            cur.next = cls(i)
            cur = cur.next
        return dummy.next

    def __repr__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)


def spiralMatrix(m: int, n: int, head: ListNode | None) -> list[list[int]]:
    res = [[-1] * n for _ in range(m)]
    i, j = 0, 0
    cur_d = 0
    movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while head:
        res[i][j] = head.val
        new_i = i + movement[cur_d][0]
        new_j = j + movement[cur_d][1]

        if min(new_i, new_j) < 0 or new_i >= m or new_j >= n or res[new_i][new_j] != -1:
            cur_d = (cur_d + 1) % 4
        i += movement[cur_d][0]
        j += movement[cur_d][1]
        head = head.next
    return res


if __name__ == '__main__':
    m1, n1, h1 = 3, 5, ListNode.from_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    m2, n2, h2 = 1, 4, ListNode.from_list([0, 1, 2])

    print(spiralMatrix(m1, n1, h1))
    print(spiralMatrix(m2, n2, h2))
