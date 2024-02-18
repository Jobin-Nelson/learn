"""
Created Date: 2024-02-12
Qn: Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
Link: https://leetcode.com/problems/majority-element/
Notes:
    - use boyer-moore's law or a counter
"""
from collections import Counter

def majorityElement(nums: list[int]) -> int:
    count = 0
    element = 0
    for n in nums:
        if count == 0:
            element = n
            count = 1
        elif element == n:
            count += 1
        else:
            count -= 1
    return element
    # return Counter(nums).most_common()[0][0]

if __name__ == '__main__':
    n1 = [3,2,3]
    n2 = [2,2,1,1,1,2,2]

    print(majorityElement(n1))
    print(majorityElement(n2))
