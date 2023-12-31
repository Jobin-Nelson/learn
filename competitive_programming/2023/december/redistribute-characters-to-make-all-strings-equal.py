"""
Created Date: 2023-12-30
Qn: You are given an array of strings words (0-indexed).

    In one operation, pick two distinct indices i and j, where words[i] is a
    non-empty string, and move any character from words[i] to any position in
    words[j].

    Return true if you can make every string in words equal using any number of
operations, and false otherwise.
Link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
Notes:
    - check if count of each character is divisible by length of words
"""
def makeEqual(words: list[str]) -> bool:
    count = [0] * 26
    cutoff = ord('a')
    N = len(words)
    for word in words:
        for c in word:
            count[ord(c) - cutoff] += 1
    return all(c % N == 0 for c in count)


if __name__ == '__main__':
    w1 = ["abc","aabc","bc"]
    w2 = ["ab", "a"]

    print(makeEqual(w1))
    print(makeEqual(w2))
