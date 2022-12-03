'''
Created Date: 2022-12-01
Qn: You are given a string s of even length. Split this string into two halves
    of equal lengths, and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels 
    ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains
    uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.
Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/
Notes:
    - use set to count number
'''
def halvesAreAlike(s: str) -> bool:
    vowel_set = set('aeiouAEIOU')
    N = len(s)

    return sum(i in vowel_set for i in s[:N//2]) == sum(i in vowel_set for i in s[N//2:])


if __name__ == '__main__':
    s1 = "book"
    s2 = "textbook"

    print(halvesAreAlike(s1))
    print(halvesAreAlike(s2))
