'''
Created Date: 2023-02-02
Qn: In an alien language, surprisingly, they also use English lowercase
    letters, but possibly in a different order. The order of the alphabet is
    some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of
    the alphabet, return true if and only if the given words are sorted
    lexicographically in this alien language.
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
Notes:
    - use hashmap to store the index of each characters
    - compare index of each characters of adjacent words
'''
def isAlienSorted(words: list[str], order: str) -> bool:
    map = {ch: i for i, ch in enumerate(order)}
    for i in range(1, len(words)):
        first = words[i-1]
        second = words[i]
        n = min(len(first), len(second))
        flag = False

        for j in range(n):
            if map[first[j]] < map[second[j]]:
                flag = True
                break
            elif map[first[j]] > map[second[j]]:
                return False
        if not flag and len(first) > len(second):
            return False
    return True

if __name__ == '__main__':
    w1, o1 = ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
    w2, o2 = ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
    w3, o3 = ["apple","app"], "abcdefghijklmnopqrstuvwxyz"

    print(isAlienSorted(w1, o1))
    print(isAlienSorted(w2, o2))
    print(isAlienSorted(w3, o3))
