"""
Created Date: 2024-08-05
Qn: A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct
    string present in arr. If there are fewer than k distinct strings, return
    an empty string "".

    Note that the strings are considered in the order in which they appear in
    the array.
Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/
Notes:
    - use hashmap
"""

from collections import Counter


def kthDistinct(arr: list[str], k: int) -> str:
    count = Counter(arr)
    for s in arr:
        if count[s] == 1:
            if k == 1:
                return s
            k -= 1
    return ''


if __name__ == '__main__':
    a1, k1 = ["d", "b", "c", "b", "c", "a"], 2
    a2, k2 = ["aaa", "aa", "a"], 1
    a3, k3 = ["a", "b", "a"], 3

    print(kthDistinct(a1, k1))
    print(kthDistinct(a2, k2))
    print(kthDistinct(a3, k3))
