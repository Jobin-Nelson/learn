"""
Created Date: 2024-04-07
Qn: Given a string s containing only three types of characters: '(', ')' and
    '*', return true if s is valid.

    The following rules define a valid string:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis
        ')'. '*' could be treated as a single right parenthesis ')' or a single
        left parenthesis '(' or an empty string "".

Link: https://leetcode.com/problems/valid-parenthesis-string/
Notes:
"""
def checkValidString(s; str) -> bool:

if __name__ == '__main__':
    s1 = "()"
    s2 = "(*)"
    s3 = "(*))"

    print(checkValidString(s1))
    print(checkValidString(s2))
    print(checkValidString(s3))
