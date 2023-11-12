'''
Created Date: 2023-11-09
Qn: Count Number of Homogenous Substrings - Given a string s, return the number
    of homogenous substrings of s. Since the answer may be too large, return it
    modulo 109 + 7.

    A string is homogenous if all the characters of the string are the same.

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/count-number-of-homogenous-substrings/
Notes:
    - use a very common counting trick which is to accumulate the current
      streak of numbers which gives you the number of homogenuos substrings
'''
def countHomogenous(s: str) -> int:
    res = 0
    MOD = 10 ** 9 + 7
    cur_streak = 0

    for i in range(len(s)):
        if i == 0 or s[i] == s[i-1]:
            cur_streak += 1
        else:
            cur_streak = 1
        res = (res + cur_streak) % MOD
    return res

if __name__ == '__main__':
    s1 = "abbcccaa"
    s2 = "xy"
    s3 = "zzzzz"

    print(countHomogenous(s1))
    print(countHomogenous(s2))
    print(countHomogenous(s3))
