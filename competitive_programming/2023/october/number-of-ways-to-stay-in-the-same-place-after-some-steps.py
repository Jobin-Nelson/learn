'''
Created Date: 2023-10-15
Qn: You have a pointer at index 0 in an array of size arrLen. At each step, you
    can move 1 position to the left, 1 position to the right in the array, or
    stay in the same place (The pointer should not be placed outside the array
    at any time).

    Given two integers steps and arrLen, return the number of ways such that
    your pointer is still at index 0 after exactly steps steps. Since the
    answer may be too large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
Notes:
'''
from functools import cache

def numWays(steps: int, arrLen: int) -> int:
    @cache
    def dfs(steps_remaining: int, xpos: int) -> int:
        if xpos - 0 > steps_remaining: return 0
        if xpos < 0 or xpos >= arrLen: return 0
        if steps_remaining == 0 and xpos == 0: return 1
        return sum((
            dfs(steps_remaining-1, xpos-1),
            dfs(steps_remaining-1, xpos),
            dfs(steps_remaining-1, xpos+1)
        )) % (10 ** 9 + 7)
    return dfs(steps, 0) % (10 ** 9 + 7)

if __name__ == '__main__':
    s1, a1 = 3, 2
    s2, a2 = 2, 4
    s3, a3 = 4, 2

    print(numWays(s1, a1))
    print(numWays(s2, a2))
    print(numWays(s3, a3))
