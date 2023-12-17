"""
Created Date: 2023-12-11
Qn: Given an integer array sorted in non-decreasing order, there is exactly 
    one integer in the array that occurs more than 25% of the time, return that integer.
Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Notes:
"""
import bisect

def findSpecialInteger(arr: list[int]) -> int:
    N = len(arr)
    candidates = [arr[N//4], arr[N//2], arr[3*N//4]]
    threshold = N // 4
    for candidate in candidates:
        left = bisect.bisect_left(arr, candidate)
        right = bisect.bisect_right(arr, candidate) - 1
        if right - left + 1 > threshold:
            return candidate
    return -1

    # for i in range(N - threshold):
    #     if arr[i] == arr[i+threshold]:
    #         return arr[i]
    # return -1
    # counter = {}
    # for n in arr:
    #     counter[n] = counter.get(n, 0) + 1
    #     if counter[n] > threshold:
    #         return n
    # return -1

if __name__ == '__main__':
    a1 = [1,2,2,6,6,6,6,7,10]
    a2 = [1,1]

    print(findSpecialInteger(a1))
    print(findSpecialInteger(a2))
