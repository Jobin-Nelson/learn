'''
Created Date: 2023-04-13
Qn: Given two integer arrays pushed and popped each with distinct values,
    return true if this could have been the result of a sequence of push and
    pop operations on an initially empty stack, or false otherwise.
Link: https://leetcode.com/problems/validate-stack-sequences/
Notes:
    - use stack
    - can use two pointer but passing by reference and mutating the list can be
      messy (not the best practice)
'''
def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    stack = []
    i = j = 0

    while i < len(pushed):
        stack.append(pushed[i])
        i += 1
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return not stack 

if __name__ == '__main__':
    pu1, po1 = [1,2,3,4,5], [4,5,3,2,1]
    pu2, po2 = [1,2,3,4,5], [4,3,5,1,2]

    print(validateStackSequences(pu1, po1))
    print(validateStackSequences(pu2, po2))
