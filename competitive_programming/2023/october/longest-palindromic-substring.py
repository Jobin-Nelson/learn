'''
Created Date: 2023-10-27
Qn: Given a string s, return the longest palindromic substring in s.
Link: https://leetcode.com/problems/longest-palindromic-substring/
Notes:
    - expand from centre
'''
def longestPalindrome(s: str) -> str:
    res, res_len = '', 0
    def check(l: int, r: int) -> None:
        nonlocal res, res_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 1 > res_len:
            res_len = r - l - 1
            res = s[l+1:r]
    for i in range(len(s)):
        check(i, i)
        check(i, i+1)

    return res

if __name__ == '__main__':
    s1 = "babad"
    s2 = "cbbd"

    print(longestPalindrome(s1))
    print(longestPalindrome(s2))
