"""
Created Date: 2024-04-05
Qn: Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i]
    and s[i + 1] where:

        - 0 <= i <= s.length - 2
        - s[i] is a lower-case letter and s[i + 1] is the same letter but in
          upper-case or vice-versa.

    To make the string good, you can choose two adjacent characters that make
    the string bad and remove them. You can keep doing this until the string
    becomes good.

    Return the string after making it good. The answer is guaranteed to be
    unique under the given constraints.

    Notice that an empty string is also good.
Link: https://leetcode.com/problems/make-the-string-great/
Notes:
    - use stack and difference between two cases 32
"""
def makeGood(s: str) -> str:
    res = []
    for c in s:
        if res and abs(ord(res[-1]) - ord(c)) == 32:
            res.pop()
        else:
            res.append(c)
    return ''.join(res)

if __name__ == '__main__':
    s1 = "leEeetcode"
    s2 = "abBAcC"
    s3 = "s"

    print(makeGood(s1))
    print(makeGood(s2))
    print(makeGood(s3))
