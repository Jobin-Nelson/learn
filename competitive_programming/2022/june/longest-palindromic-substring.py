'''
Created Date: 16-06-2022
Qn: Given a string s, return the longest palindromic substring in s
Link: https://leetcode.com/problems/longest-palindromic-substring/
Notes:
    - recursive check for both odd and even length palindrome
'''
def longestPalindrome(s: str) -> str:
    N = len(s)
    res, res_len = '', 0
    def check(l, r):
        nonlocal res, res_len
        while l >= 0 and r < N and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
    for i in range(N):
        # check odd
        l = r = i
        check(l, r)

        # check even
        l, r = i, i + 1
        check(l, r)

    return res

if __name__ == '__main__':
    s1, s2 = 'babad', 'cbbd'
    print(longestPalindrome(s1))
    print(longestPalindrome(s2))

