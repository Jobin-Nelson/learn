"""
Created Date: 2024-07-30
Qn: You are given a string s consisting only of characters 'a' and 'b'.

    You can delete any number of characters in s to make s balanced. s is
    balanced if there is no pair of indices (i,j) such that i < j and s[i] =
    'b' and s[j]= 'a'.

    Return the minimum number of deletions needed to make s balanced.
Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
Notes:
    - use dp with one variable
"""


def minimumDeletions(s: str) -> int:
    res = 0
    b = 0
    for c in s:
        if c == 'b':
            b += 1
        else:
            # Two cases: remove 'a' or keep 'a'
            res = min(res + 1, b)
    return res

    # Preprocessing suffix and prefix
    # N = len(s)
    # a_suffix = [0] * N
    # b_prefix = [0] * N
    #
    # aa = bb = 0
    # for i in range(N):
    #     r = N - i - 1
    #     a_suffix[r] = aa
    #     if s[r] == 'a':
    #         aa += 1
    #     b_prefix[i] = bb
    #     if s[i] == 'b':
    #         bb += 1
    # return min(a + b for a, b in zip(a_suffix, b_prefix))


if __name__ == '__main__':
    s1 = "aababbab"
    s2 = "bbaaaaabb"

    print(minimumDeletions(s1))
    print(minimumDeletions(s2))
