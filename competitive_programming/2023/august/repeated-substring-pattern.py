'''
Created Date: 2023-08-21
Qn: Given a string s, check if it can be constructed by taking a substring of
    it and appending multiple copies of the substring together.
Link: https://leetcode.com/problems/repeated-substring-pattern/
Notes:
    - concatenate s + s
    - if s is in the concatenated string, return true else false
'''
def repeatedSubstringPattern(s: str) -> bool:
    t = s + s
    return s in t[1:-1]

if __name__ == '__main__':
    s1 = "abab"
    s2 = "aba"
    s3 = "abcabcabcabc"

    print(repeatedSubstringPattern(s1))
    print(repeatedSubstringPattern(s2))
    print(repeatedSubstringPattern(s3))
