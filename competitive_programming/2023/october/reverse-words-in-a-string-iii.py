'''
Created Date: 2023-10-01
Qn: Given a string s, reverse the order of characters in each word within a
    sentence while still preserving whitespace and initial word order.
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Notes:
'''
def reverseWords(s: str ) -> str:
    return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    s1 = "Let's take LeetCode contest"
    s2 = "God Ding"

    print(reverseWords(s1))
    print(reverseWords(s2))
