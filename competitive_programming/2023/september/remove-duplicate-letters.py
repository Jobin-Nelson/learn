'''
Created Date: 2023-09-26
Qn: Given a string s, remove duplicate letters so that every letter appears
    once and only once. You must make sure your result is the smallest in
    lexicographical order among all possible results.
Link: https://leetcode.com/problems/remove-duplicate-letters/
Notes:
    - use monotonic stack to keep increasing order + count + visited
'''
def removeDuplicateLetters(s: str) -> str:
    a_int = ord('a')
    count = [0] * 26
    for c in s:
        count[ord(c) - a_int] += 1

    stack, visited = [], [0] * 26
    for c in s:
        c_ind = ord(c) - a_int
        if visited[c_ind]:
            count[c_ind] -= 1
            continue
        while stack and stack[-1] > c and count[ord(stack[-1])-a_int] > 0:
            visited[ord(stack[-1]) - a_int] = 0
            stack.pop()
        stack.append(c)
        visited[c_ind] = 1
        count[c_ind] -= 1
    return ''.join(stack)

if __name__ == '__main__':
    s1 = "bcabc"
    s2 = "cbacdcbc"

    print(removeDuplicateLetters(s1))
    print(removeDuplicateLetters(s2))
