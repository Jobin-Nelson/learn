"""
Created Date: 2023-12-02
Qn: You are given an array of strings words and a string chars.

    A string is good if it can be formed by characters from chars (each
    character can only be used once).

    Return the sum of lengths of all good strings in words.
Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Notes:
    - use array to keep count of chars
"""
def countCharacters(words: list[str], chars: str) -> int:
    count = [0] * 26
    for c in chars:
        count[ord(c) - ord('a')] += 1

    res = 0
    for word in words:
        cur_count = [0] * 26
        for c in word:
            idx = ord(c) - ord('a')
            cur_count[idx] += 1
            if cur_count[idx] > count[idx]:
                break
        else:
            res += len(word)
    return res

if __name__ == '__main__':
    w1, c1 = ["cat","bt","hat","tree"], "atach"
    w2, c2 = ["hello","world","leetcode"], "welldonehoneyr"

    print(countCharacters(w1, c1))
    print(countCharacters(w2, c2))
