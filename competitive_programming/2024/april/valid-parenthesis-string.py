"""
Created Date: 2024-04-07
Qn: Given a string s containing only three types of characters: '(', ')' and
    '*', return true if s is valid.

    The following rules define a valid string:

        - Any left parenthesis '(' must have a corresponding right parenthesis
          ')'.
        - Any right parenthesis ')' must have a corresponding left parenthesis
          '('.
        - Left parenthesis '(' must go before the corresponding right
          parenthesis ')'. 
        - '*' could be treated as a single right parenthesis ')' or a single
          left parenthesis '(' or an empty string "".

Link: https://leetcode.com/problems/valid-parenthesis-string/
Notes:
    - use count or stack to keep track of indexes
"""
def checkValidString(s: str) -> bool:
    open_count = 0
    close_count = 0
    length = len(s) - 1

    for i in range(length + 1):
        if s[i] == '(' or s[i] == '*':
            open_count += 1
        else:
            open_count -= 1

        if s[length - i] == ')' or s[length -i] == '*':
            close_count += 1
        else:
            close_count -= 1

        if open_count < 0 or close_count < 0:
            return False
    return True
    # left = []
    # star = []
    # for i, c in enumerate(s):
    #     if c == '(':
    #         left.append(i)
    #     elif c== '*':
    #         star.append(i)
    #     else:
    #         if left:
    #             left.pop()
    #         elif star:
    #             star.pop()
    #         else:
    #             return False
    # while left and star:
    #     if left.pop() > star.pop():
    #         return False
    # return not left

if __name__ == '__main__':
    s1 = "()"
    s2 = "(*)"
    s3 = "(*))"
    s4 = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

    print(checkValidString(s1))
    print(checkValidString(s2))
    print(checkValidString(s3))
    print(checkValidString(s4))
