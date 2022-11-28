'''
Created Date: 2022-10-10
Qn: Given a palindromic string of lowercase English letters palindrome, replace
    exactly one character with any lowercase English letter so that the
    resulting string is not a palindrome and that it is the lexicographically
    smallest one possible.

    Return the resulting string. If there is no way to replace a character to
    make it not a palindrome, return an empty string.

    A string a is lexicographically smaller than a string b (of the same
    length) if in the first position where a and b differ, a has a character
    strictly smaller than the corresponding character in b. For example, "abcc"
    is lexicographically smaller than "abcd" because the first position they
    differ is at the fourth character, and 'c' is smaller than 'd'.
Link: https://leetcode.com/problems/break-a-palindrome/
Notes:
    - change the first non 'a' to 'a'
    - if everything is 'a' change the last character to 'b'
    - return '' if length of string is 1
'''
def breakPalindrome(palindrome: str) -> str:
    p = list(palindrome)
    N = len(p)
    if N == 1: return ''
    for i in range(N):
        j = N - 1 - i
        if i == j: continue
        if p[i] != 'a': 
            p[i] = 'a'
            return ''.join(p)
    p[N-1] = 'b'
    return ''.join(p)

if __name__ == '__main__':
    p1, p2 = "abccba", "a"

    print(breakPalindrome(p1))
    print(breakPalindrome(p2))
