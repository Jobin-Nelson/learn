'''
Created Date: 2023-02-01
Qn: For two strings s and t, we say "t divides s" if and only if s = t + ... +
    t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x
    divides both str1 and str2.
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
Notes:
    - use greatest common divisor
    - when both strings are combined in either way results in the same string
      then a common divisor string exists
    - calculate the gcd with the string lengths
'''
def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(a: int, b: int) -> int:
        while a:
            a, b = b % a, a
        return b

    if str1 + str2 != str2 + str1: return ''

    max_length = gcd(len(str1), len(str2))

    return str1[:max_length]

if __name__ == '__main__':
    s11, s12 = "ABCABC", "ABC"
    s21, s22 = "ABABAB", "ABAB"
    s31, s32 = "LEET", "CODE"

    print(gcdOfStrings(s11, s12))
    print(gcdOfStrings(s21, s22))
    print(gcdOfStrings(s31, s32))
