"""
Created Date: 2024-04-06
Qn: Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in
    any positions ) so that the resulting parentheses string is valid and
    return any valid string.

    Formally, a parentheses string is valid if and only if:

        - It is the empty string, contains only lowercase characters, or
        - It can be written as AB (A concatenated with B), where A and B are
          valid strings, or
        - It can be written as (A), where A is a valid string.

Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Notes:
    - iterate left to right and remove closing parenthesis
    - iterate right to left and remove opening parenthesis
"""
def minRemoveToMakeValid(s: str) -> str:
    res = []
    left = 0
    for c in s:
        if c == '(':
            res.append(c)
            left += 1
        elif c == ')' and left > 0:
            res.append(c)
            left -= 1
        elif c != ')':
            res.append(c)
    filtered = []

    for c in reversed(res):
        if c == '(' and left > 0:
            left -= 1
        else:
            filtered.append(c)

    return ''.join(reversed(filtered))

if __name__ == '__main__':
    s1 = "lee(t(c)o)de)"
    s2 = "a)b(c)d"
    s3 = "))(("

    print(minRemoveToMakeValid(s1))
    print(minRemoveToMakeValid(s2))
    print(minRemoveToMakeValid(s3))
