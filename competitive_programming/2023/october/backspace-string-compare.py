'''
Created Date: 2023-10-19
Qn: Given two strings s and t, return true if they are equal when both are
    typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
Link: https://leetcode.com/problems/backspace-string-compare/
Notes:
    - you can use stack or two pointers and iterate reversed
'''
from itertools import zip_longest
from typing import Generator

def backspaceCompare(s: str, t: str) -> bool:
    def build(s: str) -> Generator[str, None, None]:
        skip = 0
        for c in reversed(s):
            if c == '#': skip += 1
            elif skip: skip -= 1
            else: yield c
    return all(i == j for i, j in zip_longest(build(s), build(t)))

    # i, j = len(s) - 1, len(t) - 1
    # while i >= 0 or j >= 0:
    #     while i >= 0 and s[i] == '#': i -= 2
    #     while j >= 0 and t[j] == '#': j -= 2
    #     if i >= 0 and j >= 0 and s[i] != t[j]: return False
    #     i, j = i - 1, j - 1
    # return True

    # def typewriter(s: str) -> list[int]:
    #     res = []
    #     for c in s:
    #         if c == '#':
    #             if res: res.pop()
    #             continue
    #         res.append(c)
    #     return res
    # return typewriter(s) == typewriter(t)


if __name__ == '__main__':
    s1, t1 = 'ab#c', 'ad#c'
    s2, t2 = 'ab##', 'c#d#'
    s3, t3 = 'a#c', 'b'

    print(backspaceCompare(s1, t1))
    print(backspaceCompare(s2, t2))
    print(backspaceCompare(s3, t3))
