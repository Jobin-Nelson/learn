'''
Created Date: 2023-11-03
Qn: You are given an integer array target and an integer n.

    You have an empty stack with the two following operations:

        - "Push": pushes an integer to the top of the stack. 
        - "Pop": removes the integer on the top of the stack.

    You also have a stream of the integers in the range [1, n].

    Use the two stack operations to make the numbers in the stack (from the bottom
    to the top) equal to target. You should follow the following rules:

        - If the stream of the integers is not empty, pick the next integer
          from the stream and push it to the top of the stack. 
        - If the stack is not empty, pop the integer at the top of the stack. 
        - If, at any moment, the elements in the stack (from the bottom to the
          top) are equal to target, do not read new integers from the stream
          and do not do more operations on the stack.

    Return the stack operations needed to build target following the mentioned
    rules. If there are multiple valid answers, return any of them.
Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
Notes:
    - simulate
'''
def buildArray(target: list[int], n: int) -> list[str]:
    push, pop = 'Push', 'Pop'
    res = []

    i = 1
    for n in target:
        while i < n:
            res.append(push)
            res.append(pop)
            i += 1
        res.append(push)
        i += 1
    return res

if __name__ == '__main__':
    t1, n1 = [1,3], 3
    t2, n2 = [1,2,3], 3
    t3, n3 = [1,2], 4

    print(buildArray(t1, n1))
    print(buildArray(t2, n2))
    print(buildArray(t3, n3))
