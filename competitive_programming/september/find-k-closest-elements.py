'''
Created Date: 2022-09-29
Qn: Given a sorted integer array arr, two integers k and x, return the k
    closest integers to x in the array. The result should also be sorted in
    ascending order.

    An integer a is closer to x than an integer b if:
Link: https://leetcode.com/problems/find-k-closest-elements/
Notes:
    - binary search with a window in mind
'''
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    l, r = 0, len(arr)-k 

    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m+k] - x:
            l = m + 1
        else:
            r = m

    return arr[l:l+k]

if __name__ == '__main__':
    a1, k1, x1 = [1, 2, 3, 4, 5], 4, 3
    a2, k2, x2 = [1, 2, 3, 4, 5], 4, -1

    print(findClosestElements(a1, k1, x1))
    print(findClosestElements(a2, k2, x2))
