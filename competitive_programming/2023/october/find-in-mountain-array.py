'''
Created Date: 2023-10-12
Qn: You may recall that an array arr is a mountain array if and only if:

        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Given a mountain array mountainArr, return the minimum index such that
    mountainArr.get(index) == target. If such an index does not exist, return
    -1.

    You cannot access the mountain array directly. You may only access the
    array using a MountainArray interface:

        - MountainArray.get(k) returns the element of the array at index k
          (0-indexed). 
        - MountainArray.length() returns the length of the array.

    Submissions making more than 100 calls to MountainArray.get will be judged
    Wrong Answer. Also, any solutions that attempt to circumvent the judge will
    result in disqualification.
Link: https://leetcode.com/problems/find-in-mountain-array/
Notes:
    - use binary search
'''

class MountainArray:
    def __init__(self, arr: list[int]):
        self.mountain = arr
    def get(self, index: int) -> int:
        return self.mountain[index]
    def length(self) -> int:
        return len(self.mountain)

def findInMountainArray(target: int, mountain_arr: MountainArray) -> int:
    length = mountain_arr.length()
    l, r = 1,length - 2
    while l < r:
        m = l + ((r-l) >> 1)
        cur = mountain_arr.get(m)
        nex = mountain_arr.get(m+1)
        if cur < nex:
            if cur == target: return m
            if nex == target: return m + 1
            l = m + 1
        else:
            r = m
    peak = l

    l, r = 0, peak
    while l <= r:
        m = l + ((r-l) >> 1)
        cur = mountain_arr.get(m)
        if cur < target:
            l = m + 1
        elif cur > target:
            r = m - 1
        else:
            return m

    l, r = peak + 1, length - 1
    while l <= r:
        m = l + ((r-l) >> 1)
        cur = mountain_arr.get(m)
        if cur < target:
            r = m - 1
        elif cur > target:
            l = m + 1
        else:
            return m
    return -1

if __name__ == '__main__':
    a1, t1 = MountainArray([1,2,3,4,5,3,1]), 3
    a2, t2 = MountainArray([0,1,2,4,2,1]), 3
    a3, t3 = MountainArray([1,5,2]), 2

    print(findInMountainArray(t1, a1))
    print(findInMountainArray(t2, a2))
    print(findInMountainArray(t3, a3))
