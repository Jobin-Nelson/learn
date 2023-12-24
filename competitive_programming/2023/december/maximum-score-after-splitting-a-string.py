"""
Created Date: 2023-12-22
Qn: Given a string s of zeros and ones, return the maximum score after
    splitting the string into two non-empty substrings (i.e. left substring and
    right substring).

    The score after splitting a string is the number of zeros in the left
    substring plus the number of ones in the right substring.
Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
Notes:
    - use equation score = Zl + Or = Zl + Ot - Ol = OT + (Zl - Ol)
    - Zl = left zeros
    - Or = right ones
    - Ot = total ones
"""
def maxScore(s: str) -> int:
    ones, zeros = 0, 0
    best = float('-inf')
    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
        best = max(best, zeros - ones)
    if s[-1] == '1': ones += 1
    return best + ones
    # N = len(s)
    # if N == 2: return (s[0] == '0') + (s[1] == '1')
    # zero_prefix = [0] * (N + 1)
    # one_prefix = [0] * (N + 1)
    #
    # for i in range(N):
    #     lp = i + 1
    #     rp = N - i - 1
    #     zero_prefix[lp] = zero_prefix[lp-1] + (1 if s[i] == '0' else 0)
    #     one_prefix[rp] = one_prefix[rp+1] + (1 if s[rp] == '1' else 0)
    # return max(zero_prefix[i] + one_prefix[i] for i in range(1, N))

if __name__ == '__main__':
    s1 = "011101"
    s2 = "00111"
    s3 = "1111"
    s4 = "01001"

    print(maxScore(s1))
    print(maxScore(s2))
    print(maxScore(s3))
    print(maxScore(s4))
