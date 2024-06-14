"""
Created Date: 2024-06-04
Qn: Given a string s which consists of lowercase or uppercase letters, return
    the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a
    palindrome.
Link: https://leetcode.com/problems/longest-palindrome/
Notes:
    - use hashmap
"""
from collections import Counter

def longestPalindrome(s: str) -> int:
    count = Counter(s)
    res = 0
    has_odd_freq = 0
    for v in count.values():
        if v & 1 == 0:
            res += v
        else:
            res += v - 1
            has_odd_freq = 1

    return res + has_odd_freq

if __name__ == '__main__':
    s1 = "abccccdd"
    s2 = "a"

    print(longestPalindrome(s1))
    print(longestPalindrome(s2))
