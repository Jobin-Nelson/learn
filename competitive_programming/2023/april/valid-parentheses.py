'''
Created Date: 2023-04-10
Qn: Given a string s containing just the characters '(', ')', '{', '}', '[' and
    ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Link: https://leetcode.com/problems/valid-parentheses/
Notes:
    - use map to store closing brackets
    - use stack to store opening brackets
    - when you encounter a closing bracket, pop the stack and compare 
'''
def isValid(s: str) -> bool:
    map = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    stack = []

    for p in s:
        if p in map:
            if not stack or stack.pop() != map[p]:
                return False
        else:
            stack.append(p)
    return not stack

if __name__ == '__main__':
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"

    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))
