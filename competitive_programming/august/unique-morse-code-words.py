'''
Created Date: 17-08-2022
Qn: Given an array of strings words where each word can be written as a
    concatenation of the Morse code of each letter.

    - For example, "cab" can be written as "-.-..--...", which is the
      concatenation of "-.-.", ".-", and "-...". We will call such a
      concatenation the transformation of a word.

    Return the number of different transformations among all words we have.
Link: https://leetcode.com/problems/unique-morse-code-words/
Notes:
    - hashset to collect only unique morse code
'''
def uniqueMorseRepresentations(words: list[str]) -> int:
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_set = set()

    for word in words:
        cur_code = ''
        for char in word:
            cur_code += morse_code[ord(char)-97]
        morse_set.add(cur_code)

    return len(morse_set)

if __name__ == '__main__':
    w1 = ['gin', 'zen', 'gig', 'msg']
    w2 = ['a']
    print(uniqueMorseRepresentations(w1))
    print(uniqueMorseRepresentations(w2))
