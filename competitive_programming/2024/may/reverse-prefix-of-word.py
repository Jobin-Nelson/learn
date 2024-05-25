"""
Created Date: 2024-05-01
Qn: Given a 0-indexed string word and a character ch, reverse the segment of
    word that starts at index 0 and ends at the index of the first occurrence
    of ch (inclusive). If the character ch does not exist in word, do nothing.

        - For example, if word = "abcdefd" and ch = "d", then you should
          reverse the segment that starts at 0 and ends at 3 (inclusive). The
          resulting string will be "dcbaefd".

    Return the resulting string.
Link: https://leetcode.com/problems/reverse-prefix-of-word/
Notes:
"""
def reversePrefix(word: str, ch: str) -> str:
    for i, c in enumerate(word):
        if c == ch:
            return word[i::-1] + word[i+1:]
    return word
    # try:
    #     i = word.index(ch)
    #     return word[:i+1:-1] + word[i+1:]
    # except ValueError:
    #     return word

if __name__ == '__main__':
    w1, c1 = "abcdefd", "d"
    w2, c2 = "xyxzxe", "z"
    w3, c3 = "abcd", "z"

    print(reversePrefix(w1, c1))
    print(reversePrefix(w2, c2))
    print(reversePrefix(w3, c3))
