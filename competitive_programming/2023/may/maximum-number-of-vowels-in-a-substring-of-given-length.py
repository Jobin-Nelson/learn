'''
Created Date: 2023-05-05
Qn: Given a string s and an integer k, return the maximum number of vowel
    letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Notes:
    - use fixed sliding window
'''
def maxVowels(s: str, k: int) -> int:
    res = 0
    vowels = { 'a', 'e', 'i', 'o', 'u' }

    l, r = 0, 0
    cur_max = 0
    while r < len(s):
        if s[r] in vowels:
            cur_max += 1
        if (r -l)  == k:
            if s[l] in vowels:
                cur_max -= 1
            l += 1
        res = max(res, cur_max)
        r += 1
    return res

if __name__ == '__main__':
    s1, k1 = "abciiidef", 3
    s2, k2 = "aeiou", 2
    s3, k3 = "leetcode", 3

    print(maxVowels(s1, k1))
    print(maxVowels(s2, k2))
    print(maxVowels(s3, k3))
