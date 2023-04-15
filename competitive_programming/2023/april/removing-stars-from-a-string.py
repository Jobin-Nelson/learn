'''
Created Date: 2023-04-11
Qn: You are given a string s, which contains stars *.

    In one operation, you can:

        - Choose a star in s. 
        - Remove the closest non-star character to its left, as well as remove
          the star itself.

    Return the string after all stars have been removed.

    Note:

        - The input will be generated such that the operation is always
          possible. 
        - It can be shown that the resulting string will always be unique.

Link: https://leetcode.com/problems/removing-stars-from-a-string/
Notes:
    - use stack
    - pop when you encounter *
'''
def removeStars(s: str) -> str:
    res = []
    for c in s:
        if c == '*':
            res.pop()
        else:
            res.append(c)
    return ''.join(res)

if __name__ == '__main__':
    s1 = "leet**cod*e"
    s2 = "erase*****"

    print(removeStars(s1))
    print(removeStars(s2))
