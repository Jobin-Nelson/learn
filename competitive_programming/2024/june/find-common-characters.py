"""
Created Date: 2024-06-05
Qn: Given a string array words, return an array of all characters that show up
    in all strings within the words (including duplicates). You may return the
    answer in any order.
Link: https://leetcode.com/problems/find-common-characters/
Notes:
    - use hashmap or array
"""
def commonChars(words: list[str]) -> list[str]:
    N = 26
    cutoff = ord('a')

    prev = [0] * N
    for c in words[0]:
        prev[ord(c) - cutoff] += 1

    for word in words[1:]:
        cur = [0] * N
        for c in word:
            id = ord(c) - cutoff
            cur[id] = min(cur[id]+1, prev[id])
        prev = cur
    return [chr(i+cutoff) for i, c in enumerate(prev) for _ in range(c)]

if __name__ == '__main__':
    w1 = ["bella","label","roller"]
    w2 = ["cool","lock","cook"]

    print(commonChars(w1))
    print(commonChars(w2))
