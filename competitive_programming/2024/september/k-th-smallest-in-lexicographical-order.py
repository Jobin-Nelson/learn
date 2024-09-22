"""
Created Date: 2024-09-22
Qn: Given two integers n and k, return the kth lexicographically smallest
    integer in the range [1, n].
Link: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
Notes:
"""


def findKthNumber(n: int, k: int) -> int:
    cur = 1
    i = 1

    def count(cur: int) -> int:
        res = 0
        nei = cur + 1
        while cur <= n:
            res += min(nei, n + 1) - cur
            cur *= 10
            nei *= 10
        return res

    while i < k:
        steps = count(cur)
        if i + steps <= k:
            cur += 1
            i += steps
        else:
            cur *= 10
            i += 1
    return cur


if __name__ == '__main__':
    n1, k1 = 13, 2
    n2, k2 = 1, 1

    print(findKthNumber(n1, k1))
    print(findKthNumber(n2, k2))
