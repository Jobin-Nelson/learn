'''
Created Date: 2022-12-03
Qn: Given a string s, sort it in decreasing order based on the frequency of the
    characters. The frequency of a character is the number of times it appears
    in the string.

    Return the sorted string. If there are multiple answers, return any of
    them.
Link: https://leetcode.com/problems/sort-characters-by-frequency/
Notes:
    - use hashmap, counter
'''
from collections import Counter

def frequencySort(s: str) -> str:
    return ''.join([k*v for k, v in Counter(s).most_common()])

if __name__ == '__main__':
    s1 = "tree"
    s2 = "cccaaa"
    s3 = "Aabb"

    print(frequencySort(s1))
    print(frequencySort(s2))
    print(frequencySort(s3))
