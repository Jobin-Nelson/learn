"""
Created Date: 2024-02-10
Qn: Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
Link: https://leetcode.com/problems/palindromic-substrings/
Notes:
    - check odd and even palindrome from the middle
"""
def countSubstrings(s: str) -> int:
    def check(l: int, r: int) -> int:
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
            
    res = 0
    for i in range(len(s)):
        res += check(i, i) + check(i, i+1)
    return res
        

if __name__ == '__main__':
    s1 = "abc"
    s2 = "aaa"

    print(countSubstrings(s1))
    print(countSubstrings(s2))
