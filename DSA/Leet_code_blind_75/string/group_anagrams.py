'''
Qn: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Link: https://leetcode.com/problems/group-anagrams/
Notes:
- hashmap with defaultdict(list) and the counter as keys to group the anagrams together
'''
from collections import defaultdict

def group_anagrams(s: list[str]) -> list[list[str]]:
    hashmap = defaultdict(list)

    for w in s:
        count = [0] * 26

        for c in w:
            count[ord(c) - ord('a')] += 1
        
        hashmap[tuple(count)].append(w)
    return hashmap.values()

    
if __name__ == '__main__':
    s1, s2, s3 = ["eat","tea","tan","ate","nat","bat"], [''], ['a']
    print(group_anagrams(s1))
    print(group_anagrams(s2))
    print(group_anagrams(s3))