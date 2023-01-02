'''
Created Date: 2023-01-01
Qn: Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a
    letter in pattern and a non-empty word in s.
Link: https://leetcode.com/problems/word-pattern/
Notes:
    - rules for bijections
    - num of distinct elements should be same on both sets and combined
'''
from itertools import zip_longest

def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()

    return (len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s))))

if __name__ == '__main__':
    p1, s1 = "abba", "dog cat cat dog"
    p2, s2 = "abba", "dog cat cat fish"
    p3, s3 = "aaaa", "dog cat cat dog"

    print(wordPattern(p1, s1))
    print(wordPattern(p2, s2))
    print(wordPattern(p3, s3))
