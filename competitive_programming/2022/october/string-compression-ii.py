'''
Created Date: 2022-10-15
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
    - recursive solution
    - at each iteration if the last char matches the cur char
        - incremenet if last_count is in [1, 9, 99]
    - if the last char doesn't match the cur char
        - you can choose not delete this char
        - you can choose to delete this char
        - find out which one is gives you the minimum output
'''
from functools import lru_cache

def getLengthOfOptimalCompression(s: str, k: int) -> int:
    @lru_cache
    def counter(start, last, last_count, left):
        if left < 0: return float('inf')
        if start >= len(s): return 0

        if s[start] == last:
            incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
            return incr + counter(start+1, last, last_count+1, left)
        else:
            keep_counter = 1 + counter(start+1, s[start], 1, left)
            del_counter = counter(start+1, last, last_count, left-1)
            return min(keep_counter, del_counter)
    return counter(0, "", 0, k)

if __name__ == '__main__':
    s1, k1 = "aaabcccd", 2
    s2, k2 = "aabbaa", 2
    s3, k3 = "aaaaaaaaaaa", 0

    print(getLengthOfOptimalCompression(s1, k1))
    print(getLengthOfOptimalCompression(s2, k2))
    print(getLengthOfOptimalCompression(s3, k3))
