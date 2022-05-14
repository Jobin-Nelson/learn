'''
Qn: Given an integer array nums, return true if any values appears at least twice in the array and return false if every element is distinct
Link: https://leetcode.com/problems/contains-duplicate/
Notes: 
- Put each element in a set if any element is found in the set while iterating return True else False
- Alternatively you could check the length of arr with the length of its set
'''

def contains_duplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False

def has_duplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    return True

if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    print(contains_duplicate(nums1))
    print(has_duplicate(nums2))
