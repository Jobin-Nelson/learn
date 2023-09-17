'''
Created Date: 2023-09-12
Qn: A string s is called good if there are no two different characters in s
    that have the same frequency.

    Given a string s, return the minimum number of characters you need to
    delete to make s good.

    The frequency of a character in a string is the number of times it appears
    in the string. For example, in the string "aab", the frequency of 'a' is 2,
    while the frequency of 'b' is 1.
Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
Notes:
    - use hashmap to count the frequencies
    - mark used frequencies with set and decrement when there exists a frequency
'''
from collections import Counter, defaultdict

def minDeletions(s: str) -> int:
    count, used_freq = Counter(s), set()

    res = 0
    for c, f in count.items():
        while f > 0  and f in used_freq:
            f -= 1
            res += 1
        used_freq.add(f)
    return res

if __name__ == '__main__':
    s1 = "aab"
    s2 = "aaabbbcc"
    s3 = "ceabaacb"

    print(minDeletions(s1))
    print(minDeletions(s2))
    print(minDeletions(s3))

