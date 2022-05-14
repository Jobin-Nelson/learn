'''
Qn: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Link: https://leetcode.com/problems/valid-palindrome/
Notes: 
- create a new string removing all non-alphanumeric characters and all lowercase
- compare it with reversed string
'''

def is_palindrome(s: str) -> bool:
    a = ''    

    for c in s.lower():
        if c.isalnum():
            a += c
    return a == a[::-1]

if __name__ == '__main__':
    s1, s2, s3 = "A man, a plan, a canal: Panama", "race a car", " "
    print(is_palindrome(s1))
    print(is_palindrome(s2))
    print(is_palindrome(s3))