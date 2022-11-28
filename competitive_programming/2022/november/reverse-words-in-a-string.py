'''
Created Date: 2022-11-13
Qn: Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s
    will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single
    space.

    Note that s may contain leading or trailing spaces or multiple spaces
    between two words. The returned string should only have a single space
    separating the words. Do not include any extra spaces.
Link: https://leetcode.com/problems/reverse-words-in-a-string/
Notes:
'''
def reverseWords(s: str) -> str:
    ls = s.split()
    return ' '.join(ls[::-1])

if __name__ == '__main__':
    s1 = "the sky is blue"
    s2 = "  hello world  "
    s3 = "a good   example"

    print(reverseWords(s1))
    print(reverseWords(s2))
    print(reverseWords(s3))
