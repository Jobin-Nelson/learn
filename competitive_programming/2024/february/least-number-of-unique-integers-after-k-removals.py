"""
Created Date: 2024-02-16
Qn: Given an array of integers arr and an integer k. Find the least number of
    unique integers after removing exactly k elements.
Link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
Notes:
    - decrement from the sorted list of frequencies in the reverse order
    - use minheap or bucket sort list
"""
from collections import Counter

def findLeastNumOfUniqueInts(arr: list[int], k: int) -> int:
    c = Counter(arr)
    freq_list = [0] * (len(arr) + 1)

    for f in c.values():
        freq_list[f] += 1

    res = len(c)
    for f in range(1, len(freq_list)):
        remove = freq_list[f]
        if k >= f * remove:
            k -= f * remove
            res -= remove
        else:
            remove = k // f
            res -= remove
            break
    return res
    # c = Counter(arr)
    # res = len(c)
    # for _, v in reversed(c.most_common()):
    #     k -= v
    #     if k < 0: break
    #     res -= 1
    #     if k == 0: break
    # return res

if __name__ == '__main__':
    a1, k1 = [5,5,4], 1
    a2, k2 = [4,3,1,1,3,3,2], 3

    print(findLeastNumOfUniqueInts(a1, k1))
    print(findLeastNumOfUniqueInts(a2, k2))
