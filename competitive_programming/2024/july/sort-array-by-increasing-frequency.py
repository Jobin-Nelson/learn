"""
Created Date: 2024-07-23
Qn: Given an array of integers nums, sort the array in increasing order based
    on the frequency of the values. If multiple values have the same frequency,
    sort them in decreasing order.

    Return the sorted array.
Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/
Notes:
"""
from collections import Counter

def frequencySort(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))

if __name__ == '__main__':
    n1 = [1,1,2,2,2,3]
    n2 = [2,3,1,3,2]
    n3 = [-1,1,-6,4,5,-6,1,4,1]

    print(frequencySort(n1))
    print(frequencySort(n2))
    print(frequencySort(n3))
