'''
Created Date: 2022-11-10
Qn: You are given a string s consisting of lowercase English letters. A
    duplicate removal consists of choosing two adjacent and equal letters and
    removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made.
    It can be proven that the answer is unique.
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Notes:
    - use stack
    - pop when you the character is equal to the last element in your stack
    - append otherwise
    - return the leftover elements in the stack
'''
def removeDuplicates(s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

if __name__ == '__main__':
    s1 = "abbaca"
    s2 = "azxxzy"

    print(removeDuplicates(s1))
    print(removeDuplicates(s2))
