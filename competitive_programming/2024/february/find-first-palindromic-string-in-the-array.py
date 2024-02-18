"""
Created Date: 2024-02-13
Qn: Given an array of strings words, return the first palindromic string in the
    array. If there is no such string, return an empty string "".

    A string is palindromic if it reads the same forward and backward.
Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
Notes:
    - filter and return the first value
"""
def firstPalindrome(words: list[str]) -> str:
    return next(filter(lambda x: x == x[::-1], words), '')
    # def is_palindrome(word: str) -> bool:
    #     l, r = 0, len(word)-1
    #     while l < r and word[l] == word[r]:
    #         l += 1
    #         r -= 1
    #     return l >= r
    # return next(filter(is_palindrome, words), '')


if __name__ == '__main__':
    w1 = ["abc","car","ada","racecar","cool"]
    w2 = ["notapalindrome","racecar"]
    w3 = ["def","ghi"]

    print(firstPalindrome(w1))
    print(firstPalindrome(w2))
    print(firstPalindrome(w3))
