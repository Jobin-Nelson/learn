"""
Created Date: 2024-02-01
Qn: You are given an integer array nums of size n and a positive integer k.

    Divide the array into one or more arrays of size 3 satisfying the following
    conditions:

        - Each element of nums should be in exactly one array. 
        - The difference between any two elements in one array is less than or
          equal to k.

    Return a 2D array containing all the arrays. If it is impossible to satisfy
    the conditions, return an empty array. And if there are multiple answers,
    return any of them.
Link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
Notes:
    - sort and group them
"""
def divideArray(nums: list[int], k: int) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(0, len(nums), 3):
        if nums[i+2] - nums[i] > k:
            return []
        res.append(nums[i:i+3])
    return res

if __name__ == '__main__':
    n1, k1 = [1,3,4,8,7,9,3,5,1], 2
    n2, k2 = [1,3,3,2,7,3], 3

    print(divideArray(n1, k1))
    print(divideArray(n2, k2))
