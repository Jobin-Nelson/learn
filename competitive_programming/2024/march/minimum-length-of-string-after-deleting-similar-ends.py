"""
Created Date: 2024-03-05
Qn: Given a string s consisting only of characters 'a', 'b', and 'c'. You are
    asked to apply the following algorithm on the string any number of times:

        - Pick a non-empty prefix from the string s where all the characters in
          the prefix are equal. 
        - Pick a non-empty suffix from the string s where all the characters in
          this suffix are equal. 
        - The prefix and the suffix should not intersect at any index. 
        - The characters from the prefix and suffix must be the same. 
        - Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any
    number of times (possibly zero times).
Link: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
Notes:
    - use two pointer
"""
def minimumLength(s: str) -> int:
    l, r = 0, len(s) - 1

    while l < r and s[l] == s[r]:
        c = s[l]
        l += 1
        r -= 1
        while l<=r and s[l] == c:
            l += 1
        while l<=r and s[r] == c:
            r -= 1
    return r - l + 1

if __name__ == '__main__':
    s1 = "ca"
    s2 = "cabaabac"
    s3 = "aabccabba"
    s4 = "ca"

    print(minimumLength(s1))
    print(minimumLength(s2))
    print(minimumLength(s3))
    print(minimumLength(s4))
