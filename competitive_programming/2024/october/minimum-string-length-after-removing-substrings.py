"""
Created Date: 2024-10-07
Qn: You are given a string s consisting only of uppercase English letters.

    You can apply some operations to this string where, in one operation, you
    can remove any occurrence of one of the substrings "AB" or "CD" from s.

    Return the minimum possible length of the resulting string that you can
    obtain.

    Note that the string concatenates after removing the substring and could
    produce new "AB" or "CD" substrings.
Link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
Notes:
    - use stack
"""


def minLength(s: str) -> int:
    stack = []
    for c in s:
        if c == 'B':
            if stack and stack[-1] == 'A':
                stack.pop()
                continue
        elif c == 'D':
            if stack and stack[-1] == 'C':
                stack.pop()
                continue
        stack.append(c)

    return len(stack)


if __name__ == '__main__':
    s1 = "ABFCACDB"
    s2 = "ACBBD"

    print(minLength(s1))
    print(minLength(s2))
