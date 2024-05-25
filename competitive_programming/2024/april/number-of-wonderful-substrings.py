"""
Created Date: 2024-04-30
Qn: A wonderful string is a string where at most one letter appears an odd
    number of times.

        - For example, "ccjjc" and "abab" are wonderful, but "ab" is not.

    Given a string word that consists of the first ten lowercase English
    letters ('a' through 'j'), return the number of wonderful non-empty
    substrings in word. If the same substring appears multiple times in word,
    then count each occurrence separately.

    A substring is a contiguous sequence of characters in a string.
Link: https://leetcode.com/problems/number-of-wonderful-substrings/
Notes:
    - XOR operator is equivalent to subtractions under modulo of 2
    - use bitmask for checking parity
    - same parity means even number of characters in between
"""
def wonderfulSubstrings(word: str) -> int:
    freq = {0:1}
    res = mask = 0

    for c in word:
        ind = ord(c) - ord('a')
        mask ^= (1 << ind)
        # counting if there's only even number of characters in the substring
        res += freq.get(mask, 0)

        # checking if only one odd number is present in the substring
        for i in range(10):
            pre_mask = mask ^ (1 << i)
            res += freq.get(pre_mask, 0)
        freq[mask] = freq.get(mask, 0) + 1
    return res
    

    # N = len(word)
    # count = [0] * 10
    # l = 0
    # res = 0
    # for r in range(N):
    #     c = word[r]
    #     cind = ord(c) - ord('a')
    #     count[cind] += 1
    #     if sum(n & 1 for n in count) > 1: continue
    #     res += 
        


if __name__ == '__main__':
    w1 = "aba"
    w2 = "aabb"
    w3 = "he"

    print(wonderfulSubstrings(w1))
    print(wonderfulSubstrings(w2))
    print(wonderfulSubstrings(w3))

