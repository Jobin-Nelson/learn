'''
Created Date: 2023-01-02
Qn: We define the usage of capitals in a word to be right when one of the
    following cases holds:

        - All letters in this word are capitals, like "USA". 
        - All letters in this word are not capitals, like "leetcode". 
        - Only the first letter in this word is capital, like "Google". 

    Given a string word, return true if the usage of capitals in it is right.
Link: https://leetcode.com/problems/detect-capital/
Notes:
    - check each case
'''
def detectCapitalUse(word: str) -> bool:
    if all(c.isupper() for c in word): return True
    if all(c.islower() for c in word): return True
    if word[0].isupper() and all(c.islower() for c in word[1:]): return True
    return False


if __name__ == '__main__':
    w1 = "USA"
    w2 = "FlaG"

    print(detectCapitalUse(w1))
    print(detectCapitalUse(w2))
