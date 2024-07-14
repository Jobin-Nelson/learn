"""
Created Date: 2024-07-11
Qn: You are given a string s that consists of lower case English letters and
    brackets.

    Reverse the strings in each pair of matching parentheses, starting from the
    innermost one.

    Your result should not contain any brackets.
Link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
Notes:
    - use wormhole teleportation technique
"""
def reverseParenthesis(s: str) -> str:
    N = len(s)
    open_brackets = []
    pair = [0] * N
    for i in range(N):
        if s[i] == '(':
            open_brackets.append(i)
        elif s[i] == ')':
            j = open_brackets.pop()
            pair[i] = j
            pair[j] = i
    res = []
    cur_ind = 0
    direction = 1
    while cur_ind < N:
        if s[cur_ind] == '(' or s[cur_ind] == ')':
            cur_ind = pair[cur_ind]
            direction = -direction
        else:
            res.append(s[cur_ind])
        cur_ind += direction
    return ''.join(res)

if __name__ == '__main__':
    s1 = "(abcd)"
    s2 = "(u(love)i)"
    s3 = "(ed(et(oc))el)"

    print(reverseParenthesis(s1))
    print(reverseParenthesis(s2))
    print(reverseParenthesis(s3))

