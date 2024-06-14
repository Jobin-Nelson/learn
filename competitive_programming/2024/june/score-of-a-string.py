"""
Created Date: 2024-06-01
Qn: You are given a string s. The score of a string is defined as the sum of
    the absolute difference between the ASCII values of adjacent characters.
Link: https://leetcode.com/problems/score-of-a-string/
Notes:
"""
def scoreOfString(s: str) -> int:
    res = 0
    prev_score = ord(s[0])
    for c in s[1:]:
        cur_score = ord(c)
        res += abs(cur_score - prev_score)
        prev_score = cur_score
    return res

if __name__ == '__main__':
    s1 = "hello"
    s2 = "zaz"

    print(scoreOfString(s1))
    print(scoreOfString(s2))
