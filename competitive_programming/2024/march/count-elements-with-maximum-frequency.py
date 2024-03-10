"""
Created Date: 2024-03-06
Qn: You are given an array nums consisting of positive integers.

    Return the total frequencies of elements in nums such that those elements all
    have the maximum frequency.

    The frequency of an element is the number of occurrences of that element in the
    array.
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
Notes:
    - use dictionary
"""
from collections import defaultdict

def maxFrequency(nums: list[int]) -> int:
    frequencies = defaultdict(int)
    max_frequency = 0
    total_frequencies = 0

    for num in nums:
        frequencies[num] += 1
        frequency = frequencies[num]
        if frequency > max_frequency:
            max_frequency = frequency
            total_frequencies = frequency
        elif frequency == max_frequency:
            total_frequencies += frequency
    return total_frequencies


if __name__ == '__main__':
    n1 = [1,2,2,3,1,4]
    n2 = [1,2,3,4,5]
    n3 = [15]
    n4 = [10,12,11,9,6,19,11]

    print(maxFrequency(n1))
    print(maxFrequency(n2))
    print(maxFrequency(n3))
    print(maxFrequency(n4))
