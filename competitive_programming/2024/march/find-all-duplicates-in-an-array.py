"""
Created Date: 2024-03-25
Qn: Given an integer array nums of length n where all the integers of nums are
    in the range [1, n] and each integer appears once or twice, return an array
    of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant
    extra space.
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Notes:
    - use same array to store visited by changing the sign to negative
"""
def findDuplicates(nums: list[int]) -> list[int]:
    res = []
    for n in nums:
        id = abs(n)
        val = nums[id-1]
        if val < 0:
            res.append(id)
        else:
            nums[id-1] *= -1
    return res

if __name__ == '__main__':
    n1 = [4,3,2,7,8,2,3,1]
    n2 = [1,1,2]
    n3 = [1]

    print(findDuplicates(n1))
    print(findDuplicates(n2))
    print(findDuplicates(n3))
