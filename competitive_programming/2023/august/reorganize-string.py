'''
Created Date: 2023-08-23
Qn: Given a string s, rearrange the characters of s so that any two adjacent
    characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.
Link: https://leetcode.com/problems/reorganize-string/
Notes:
    - add most frequent letter to even positions
    - if most frequent letter count is more than half of the length of the
      string return ''
    - add the rest of the letters to remaining even and odd positions
'''
from collections import Counter

def reorganizeString(s: str) -> str:
    char_counts = Counter(s)
    max_count, max_letter = 0, ''
    N = len(s)

    for letter, count in char_counts.items():
        if count > max_count:
            max_count = count
            max_letter = letter

    if max_count > (N + 1) // 2: return ''
    res, index = [''] * N, 0
    while char_counts[max_letter] > 0:
        res[index] = max_letter
        index += 2
        char_counts[max_letter] -= 1

    for letter, count in char_counts.items():
        while count > 0:
            if index >= N: index = 1
            res[index] = letter
            index += 2
            count -= 1

    return ''.join(res)

if __name__ == '__main__':
    s1 = "aab"
    s2 = "aaab"

    print(reorganizeString(s1))
    print(reorganizeString(s2))
