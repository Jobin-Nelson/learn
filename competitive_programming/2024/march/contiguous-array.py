"""
Created Date: 2024-03-16
Qn: Given a binary array nums, return the maximum length of a contiguous
    subarray with an equal number of 0 and 1.
Link: https://leetcode.com/problems/contiguous-array/
Notes:
    - use hashmap and count variable to increment and decrement by 1 when
      encountering 1 and 0 respectively
    - if count variables is same as before or zero then we have equal number of
      1's and 0's
"""
def findMaxLength(nums: list[int]) -> int:
    lookup = { 0: -1 }
    res = count = 0
    for i, n in enumerate(nums):
        count += 1 if n == 1 else -1
        if count in lookup:
            res = max(res, i - lookup[count])
        else:
            lookup[count] = i
    return res

if __name__ == '__main__':
    n1 = [0, 1]
    n2 = [0, 1, 0]

    print(findMaxLength(n1))
    print(findMaxLength(n2))
