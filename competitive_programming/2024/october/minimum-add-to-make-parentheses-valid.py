"""
Created Date: 2024-10-09
Qn: A parentheses string is valid if and only if:

    - It is the empty string,
    - It can be written as AB (A concatenated with B), where A and B are valid
      strings, or
    - It can be written as (A), where A is a valid string.

    You are given a parentheses string s. In one move, you can insert a
    parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be
    "(()))" or a closing parenthesis to be "())))". Return the minimum number
    of moves required to make s valid.
Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
Notes:
    - count open brackets
"""


def minAddToMakeValid(s: str) -> int:
    open_brackets = 0
    min_adds_required = 0

    for c in s:
        if c == '(':
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            else:
                min_adds_required += 1
    return min_adds_required + open_brackets


if __name__ == '__main__':
    s1 = "())"
    s2 = "((("
    s3 = "()))(("

    print(minAddToMakeValid(s1))
    print(minAddToMakeValid(s2))
    print(minAddToMakeValid(s3))
