'''
Created Date: 2022-10-17
Qn: A pangram is a sentence where every letter of the English alphabet appears
    at least once.

    Given a string sentence containing only lowercase English letters, return
    true if sentence is a pangram, or false otherwise.
Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Notes:
    - check if the length of set with the string is 26
'''
import string

def checkIfPangram(sentence: str) -> bool:
    # return not set(string.ascii_lowercase).difference(set(sentence))
    return len(set(sentence)) == 26

if __name__ == '__main__':
    s1 = "thequickbrownfoxjumpsoverthelazydog"
    s2 = "leetcode"

    print(checkIfPangram(s1))
    print(checkIfPangram(s2))
