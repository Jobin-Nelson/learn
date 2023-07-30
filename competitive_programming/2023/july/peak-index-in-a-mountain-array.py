'''
Created Date: 2023-07-25
Qn: An array arr a mountain if the following properties hold:

    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Given a mountain array arr, return the index i such that arr[0] < arr[1] <
    ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    You must solve it in O(log(arr.length)) time complexity.
Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
Notes:
    - use binary search
'''
def peakIndexMountainArray(arr: list[int]) -> int:
    l, r = 0, len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[m+1]:
            l = m + 1
        else:
            r = m
    return l

if __name__ == '__main__':
    a1 = [0,1,0]
    a2 = [0,2,1,0]
    a3 = [0,10,5,2]

    print(peakIndexMountainArray(a1))
    print(peakIndexMountainArray(a2))
    print(peakIndexMountainArray(a3))
