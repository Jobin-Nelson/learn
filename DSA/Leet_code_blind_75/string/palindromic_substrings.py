'''
Qn: Given a string s, return the number of palindromic substrings in it.
Link: https://leetcode.com/problems/palindromic-substrings/
Notes:
'''

def count_substrings(s: str) -> int:
    res = 0

    def check(l, r):
        nonlocal res
        while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -=1 
                r += 1
    i = 0
    while i < len(s):
        # Odd length
        l = r = i
        check(l, r)

        # Even length
        l, r = i, i + 1
        check(l, r)
        i += 1
    return res

if __name__ == '__main__':
    s1, s2 = "abc", "aaa"
    print(count_substrings(s1))
    print(count_substrings(s2))