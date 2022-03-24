'''
Qn: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Link: https://leetcode.com/problems/valid-parentheses/
Notes:
- track the opening brackets using list (Stack)
- hashmap to compare opening with closing brackets
'''

def isValid(s: str) -> bool:
    hashmap = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []

    for c in s:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


            
if __name__ == '__main__':
    s1, s2, s3 = "()", "()[]{}", "(]"
    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))