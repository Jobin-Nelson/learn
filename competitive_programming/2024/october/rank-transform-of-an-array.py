"""
Created Date: 2024-10-02
Qn: Given an array of integers arr, replace each element with its rank.

    The rank represents how large the element is. The rank has the following
    rules:

    Rank is an integer starting from 1. The larger the element, the larger the
    rank. If two elements are equal, their rank must be the same. Rank should
    be as small as possible.
Link: https://leetcode.com/problems/rank-transform-of-an-array/
Notes:
    - use sorted arr and hashmap
"""


def arrayRankTransform(arr: list[int]) -> list[int]:
    sorted_arr = sorted(arr)
    num_to_rank = {}
    rank = 1
    for i, n in enumerate(sorted_arr):
        if i > 0 and n > sorted_arr[i - 1]:
            rank += 1
        num_to_rank[n] = rank
    return list(map(lambda x: num_to_rank[x], arr))


if __name__ == '__main__':
    a1 = [40, 10, 20, 30]
    a2 = [100] * 3
    a3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]

    print(arrayRankTransform(a1))
    print(arrayRankTransform(a2))
    print(arrayRankTransform(a3))
