'''
Qn: Given a string s, return the longest palindromic substring in s
Link: https://leetcode.com/problems/longest-palindromic-substring/
Notes:
- check from the middle of palindrome
- check for both Odd and Even palindromes
'''

def long_palindrome(s: str) -> bool:
    res = ''
    res_len = 0

    def check(l, r):
        nonlocal res
        nonlocal res_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > res_len:
                res = s[l:r+1]
                res_len = r-l+1
            l -= 1
            r += 1

    for i in range(len(s)):
        # Odd length
        l, r = i, i
        check(l, r)
        # Even length
        l, r = i, i + 1
        check(l, r)

    return res
if __name__ == '__main__':
    s1, s2 = "babad", "cbbd"
    print(long_palindrome(s1))
    print(long_palindrome(s2))