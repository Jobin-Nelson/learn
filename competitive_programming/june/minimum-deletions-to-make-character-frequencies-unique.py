'''
Created Date: 28-06-2022
Qn: A string s is called good if there are no two different characters in s that have 
    the same frequency. Given a string s, return the minimum number of characters you 
    need to delete to make s good.
    The frequency of a character in a string is the number of times it appears in the 
    string. For example, in the string "aab", the frequency of 'a' is 2, while the 
    frequency of 'b' is 1.
Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
Notes:
- increment everytime the we have same frequency character
'''
from collections import Counter

def minDeletions(s: str) -> int:
    counter = Counter(s)
    deletions, freq_set = 0, set()
    for k, v in counter.items():
        if v > 0 and v in freq_set:
            v -= 1
            deletions += 1
        freq_set.add(v)
    return deletions

if __name__ == '__main__':
    s1, s2, s3 = "aab", "aaabbbcc", "ceabaacb"
    print(minDeletions(s1))
    print(minDeletions(s2))
    print(minDeletions(s3))
