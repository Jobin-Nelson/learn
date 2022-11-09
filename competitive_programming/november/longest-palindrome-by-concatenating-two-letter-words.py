'''
Created Date: 2022-11-03
Qn: You are given an array of strings words. Each element of words consists of
    two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words
    and concatenating them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is
    impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.
Link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
Notes:
    - Things to keep track
        - pairs => actual pairs like "ab, ba"
        - non_paired => counter of all the words
        - sym => tracking even of odd number of same elements
    - Second method keeps track of 
        - aa => same elements
        - abba => not same elements
        - center => if there is odd number of same elements
'''
from collections import Counter

def longestPalindrome(words: list[str]) -> int:
    pairs, sym, non_paired = 0, 0, Counter()

    for w in words:
        if non_paired[w[::-1]] > 0:
            pairs += 1
            non_paired[w[::-1]] -= 1
            if w[0] == w[1]: sym -= 1
        else:
            non_paired[w] += 1
            if w[0] == w[1]: sym += 1
    return pairs * 4 + (2 if sym > 0 else 0)
    # wc = Counter(words)
    # aa, center, abba = 0, 0, 0
    #
    # for w, c in wc.items():
    #     if w[0] == w[1]:
    #         aa += c // 2 * 2
    #         if c % 2 == 1: center = 2
    #     else:
    #         abba += min(wc[w], wc[w[::-1]]) * 0.5
    # return aa * 2 + center + int(abba) * 4

if __name__ == '__main__':
    w1 = ["lc","cl","gg"]
    w2 = ["ab","ty","yt","lc","cl","ab"]
    w3 = ["cc","ll","xx"]

    print(longestPalindrome(w1))
    print(longestPalindrome(w2))
    print(longestPalindrome(w3))
