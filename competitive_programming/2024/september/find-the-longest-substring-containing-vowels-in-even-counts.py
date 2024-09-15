"""
Created Date: 2024-09-15
Qn: Given the string s, return the size of the longest substring containing
    each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u'
    must appear an even number of times.
Link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
Notes:
    - use bitmask
"""


def findTheLongestSubstring(s: str) -> int:
    cmap = [0] * 26
    cmap[ord('a') - ord('a')] = 1
    cmap[ord('e') - ord('a')] = 1 << 1
    cmap[ord('i') - ord('a')] = 1 << 2
    cmap[ord('o') - ord('a')] = 1 << 3
    cmap[ord('u') - ord('a')] = 1 << 4

    mp = [-1] * 32
    prefixXOR = 0
    res = 0
    for i, c in enumerate(s):
        prefixXOR ^= cmap[ord(c) - ord('a')]
        if mp[prefixXOR] == -1 and prefixXOR != 0:
            mp[prefixXOR] = i
        res = max(res, i - mp[prefixXOR])
    return res


if __name__ == '__main__':
    s1 = "eleetminicoworoep"
    s2 = "leetcodeisgreat"
    s3 = "bcbcbc"

    print(findTheLongestSubstring(s1))
    print(findTheLongestSubstring(s2))
    print(findTheLongestSubstring(s3))
