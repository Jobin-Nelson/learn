'''
Created Date: 2023-03-06
Qn: Given an array arr of positive integers sorted in a strictly increasing
    order, and an integer k.

    Return the kth positive integer that is missing from this array.
Link: https://leetcode.com/problems/kth-missing-positive-number/
Notes:
    - use binary search 
    - look for the first arr[i] - i > k
    - return i + k
'''
def findKthPositive(arr: list[int], k: int) -> int:
    l, r = 0, len(arr)
    while l < r:
        m = l + ((r - l) >> 1)
        if arr[m] - m > k:
            r = m
        else:
            l = m + 1
    return l + k

if __name__ == '__main__':
    a1, k1 = [2,3,4,7,11], 5
    a2, k2 = [1,2,3,4], 2

    print(findKthPositive(a1, k1))
    print(findKthPositive(a2, k2))
