'''
Created Date: 2023-10-03
Qn: Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
Link: https://leetcode.com/problems/number-of-good-pairs/
Notes:
    - use hashmap
'''
from collections import Counter

def numIdenticalPairs(nums: list[int]) -> int:
    return sum(c * (c-1) // 2 for _, c in Counter(nums).items())

if __name__ == '__main__':
    n1 = [1,2,3,1,1,3]
    n2 = [1,1,1,1]
    n3 = [1,2,3]

    print(numIdenticalPairs(n1))
    print(numIdenticalPairs(n2))
    print(numIdenticalPairs(n3))
