'''
Created Date: 2023-10-05
Qn: Given an integer array of size n, find all elements that appear more than ⌊
    n/3 ⌋ times.
Link: https://leetcode.com/problems/majority-element-ii/
Notes:
    - use hashmap to store most frequent 2 elements
    - decrement frequency if the len of hashmap goes over 2
    - verify and return the remaining 2 elements in the hashmap
'''
from collections import defaultdict

def majorityElement(nums: list[int]) -> list[int]:
    counts = defaultdict(int)

    for n in nums:
        counts[n] += 1
        if len(counts) <= 2: continue
        new_counts = defaultdict(int)
        for n, c in counts.items():
            if c > 1: new_counts[n] = c-1
        counts = new_counts
    return [n for n in counts if nums.count(n) > len(nums) // 3]

if __name__ == '__main__':
    n1 = [3,2,3]
    n2 = [1]
    n3 = [1,2]

    print(majorityElement(n1))
    print(majorityElement(n2))
    print(majorityElement(n3))
