'''
Qn: We repeatedly make k duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made. 
    It is guaranteed that the answer is unique.
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Notes:
    - use stack to keep track of char and count
    - pop when the count reaches k, join and return the string 
'''
from collections import deque
def removeDuplicates(s: str, k: int) -> str:
    ns = ''
    for c in s:
        ns += c
        if ns[-k:] == ns[-1]*k:
            ns = ns[:-k]
    return ns

def removeDuplicatesUsingStack(s: str, k: int) -> str: # more effecient than the above solution
    stack = [] # (char, count)
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])
        if stack[-1][1] == k:
            stack.pop()
    res = ''
    for char, count in stack:
        res += char * count
    return ''.join(res)




if __name__ == '__main__':
    s1, k1 = 'abcd', 2
    s2, k2 = 'deeedbbcccbdaa', 3
    s3, k3 = 'pbbcggttciiippooaais', 2
    print(removeDuplicates(s1, k1))
    print(removeDuplicates(s2, k2))
    print(removeDuplicates(s3, k3))
    print(removeDuplicatesUsingStack(s1, k1))
    print(removeDuplicatesUsingStack(s2, k2))
    print(removeDuplicatesUsingStack(s3, k3))
