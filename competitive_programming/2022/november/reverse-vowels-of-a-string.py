'''
Created Date: 2022-11-04
Qn: Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
    lower and upper cases, more than once.
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Notes:
    - two pointer one from left end and right end
    - iterate till you reach a vowel and then swap them
'''
def reverseVowels(s: str) -> str:
    word = list(s) 
    vowels = set(list("aeiouAEIOU"))
    l, r = 0, len(word) - 1

    while l < r:
        while l < r and word[l] not in vowels:
            l += 1
        while l < r and word[r] not in vowels:
            r -= 1
        word[l], word[r] = word[r], word[l]
        l += 1
        r -= 1
    return ''.join(word)
        
    # word = list(s)
    # vowels = set(list("aeiouAEIOU"))
    # present_vowels = [ch for ch in word if ch in vowels]
    #
    # for i, ch in enumerate(word):
    #     if ch in vowels:
    #         word[i] = present_vowels.pop()
    # return ''.join(word)

if __name__ == '__main__':
    s1 = "hello"
    s2 = "leetcode"

    print(reverseVowels(s1))
    print(reverseVowels(s2))
