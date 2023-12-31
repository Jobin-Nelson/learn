"""
Created Date: 2023-12-28
Qn: Run-length encoding is a string compression method that works by replacing
    consecutive identical characters (repeated 2 or more times) with the
    concatenation of the character and the number marking the count of the
    characters (length of the run). For example, to compress the string
    "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the
    compressed string becomes "a2bc3".

    Notice that in this problem, we are not adding '1' after single characters.

    Given a string s and an integer k. You need to delete at most k characters
    from s such that the run-length encoded version of s has minimum length.

    Find the minimum length of the run-length encoded version of s after
    deleting at most k characters.
Link: https://leetcode.com/problems/string-compression-ii/
Notes:
    - use recursion
"""
from functools import cache

def getLengthOfOptimalCompression(s: str, k: int) -> int:
    @cache
    def count(i: int, k: int, prev: str, prev_count: int) -> int:
        if k < 0: return float('inf')
        if i == len(s): return 0

        if s[i] == prev:
            incr = 1 if prev_count in [1, 9, 99] else 0
            res = incr + count(i+1, k, prev, prev_count + 1)
        else:
            res = min(
                count(i+1, k-1, prev, prev_count), # delete s[i]
                1 + count(i+1, k, s[i], 1),        # dont' delete
            )
        return res
    return count(0, k, "", 0)

if __name__ == '__main__':
    s1, k1 = "aaabcccd", 2
    s2, k2 = "aabaa", 2
    s3, k3 = "aaaaaaaaaaa", 0

    print(getLengthOfOptimalCompression(s1, k1))
    print(getLengthOfOptimalCompression(s2, k2))
    print(getLengthOfOptimalCompression(s3, k3))
