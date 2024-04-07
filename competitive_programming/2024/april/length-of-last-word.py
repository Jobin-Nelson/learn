"""
Created Date: 2024-04-01
Qn: Given a string s consisting of words and spaces, return the length of the
    last word in the string.

    A word is a maximal substring consisting of non-space characters only.
Link: https://leetcode.com/problems/length-of-last-word/
Notes:
"""
def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

if __name__ == '__main__':
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"

    print(lengthOfLastWord(s1))
    print(lengthOfLastWord(s2))
    print(lengthOfLastWord(s3))
