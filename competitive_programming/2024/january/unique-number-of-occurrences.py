"""
Created Date: 2024-01-17
Qn: Given an array of integers arr, return true if the number of occurrences of
    each value in the array is unique or false otherwise.
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Notes:
    - use set and counter to count the number of values
"""
from collections import Counter

def uniqueOccurences(arr: list[int]) -> bool:
    c = Counter(arr).values()
    return len(c) == len(set(c))

if __name__ == '__main__':
    a1 = [1,2,2,1,1,3]
    a2 = [1,2]
    a3 = [-3,0,1,-3,1,1,1,-3,10,0]

    print(uniqueOccurences(a1))
    print(uniqueOccurences(a2))
    print(uniqueOccurences(a3))
