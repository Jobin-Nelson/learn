"""
Created Date: 2024-06-11
Qn: Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
    elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1
    are the same as in arr2. Elements that do not appear in arr2 should be
    placed at the end of arr1 in ascending order.
Link: https://leetcode.com/problems/relative-sort-array/
Notes:
    - use hashmap
"""
from collections import Counter

def relativeSortyArray(arr1: list[int], arr2: list[int]) -> list[int]:
    count_a1 = Counter(arr1)
    res = []
    for n in arr2:
        res.extend([n] * count_a1[n])
        del count_a1[n]
    for k, v in sorted(count_a1.items()):
        res.extend([k] * v)
    return res

if __name__ == '__main__':
    a11, a12 = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
    a21, a22 = [28,6,22,8,44,17], [22,28,8,6]

    print(relativeSortyArray(a11 ,a12))
    print(relativeSortyArray(a21 ,a22))
