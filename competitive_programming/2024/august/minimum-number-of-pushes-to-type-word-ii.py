"""
Created Date: 2024-08-06
Qn: You are given a string word containing lowercase English letters.

    Telephone keypads have keys mapped with distinct collections of lowercase
    English letters, which can be used to form words by pushing them. For
    example, the key 2 is mapped with ["a","b","c"], we need to push the key
    one time to type "a", two times to type "b", and three times to type "c" .

    It is allowed to remap the keys numbered 2 to 9 to distinct collections of
    letters. The keys can be remapped to any amount of letters, but each letter
    must be mapped to exactly one key. You need to find the minimum number of
    times the keys will be pushed to type the string word.

    Return the minimum number of pushes needed to type word after remapping the
    keys.

    An example mapping of letters to keys on a telephone keypad is given below.
    Note that 1, *, #, and 0 do not map to any letters.
Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
Notes:
    - get frequency and sort
"""


def minimumPushes(word: str) -> int:
    count = [0] * 26
    for c in word:
        count[ord(c) - ord('a')] += 1
    count.sort(reverse=True)

    res = 0
    for i, d in enumerate(count):
        res += d * ((i>>3) + 1)
    return res


if __name__ == '__main__':
    w1 = "abcde"
    w2 = "xyzxyzxyzxyz"
    w3 = "aabbccddeeffgghhiiiiii"

    print(minimumPushes(w1))
    print(minimumPushes(w2))
    print(minimumPushes(w3))
