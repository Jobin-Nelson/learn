'''
Created Date: 08-06-2022
Qn: You are given a string s consisting only of letters 'a' and 'b'. 
    In a single step you can remove one palindromic subsequence from s.
    Return the minimum number of steps to make the given string empty.
Link: https://leetcode.com/problems/remove-palindromic-subsequences/
Notes:
    - since there are only two characters and it doesn't have to be contiguous
    - we just need to account for three cases
'''
def removePalindromeSub(s: str) -> int:
    if not s: return 0
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]: return 2
        l += 1
        r -= 1
    return 1

if __name__ == '__main__':
    s1, s2, s3 = 'ababa', 'abb', 'baabb'
    print(removePalindromeSub(s1))
    print(removePalindromeSub(s2))
    print(removePalindromeSub(s3))
