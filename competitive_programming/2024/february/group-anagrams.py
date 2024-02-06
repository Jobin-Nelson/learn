"""
Created Date: 2024-02-06
Qn: Given an array of strings strs, group the anagrams together. You can return
    the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
Link: https://leetcode.com/problems/group-anagrams/
Notes:
    - use hashmap
"""
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        res[''.join(sorted(s))].append(s)
    return list(res.values())

if __name__ == '__main__':
    s1 = ["eat","tea","tan","ate","nat","bat"]
    s2 = [""]
    s3 = ["a"]

    print(group_anagrams(s1))
    print(group_anagrams(s2))
    print(group_anagrams(s3))
