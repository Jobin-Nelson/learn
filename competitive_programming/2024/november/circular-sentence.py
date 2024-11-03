"""
Created Date: 2024-11-02
Qn: A sentence is a list of words that are separated by a single space with no
    leading or trailing spaces.

        - For example, "Hello World", "HELLO", "hello world hello world" are
          all sentences.

    Words consist of only uppercase and lowercase English letters. Uppercase
    and lowercase English letters are considered different.

    A sentence is circular if:

        - The last character of a word is equal to the first character of the
          next word.
        - The last character of the last word is equal to the first character
          of the first word.

    For example, "leetcode exercises sound delightful", "eetcode", "leetcode
    eats soul" are all circular sentences. However, "Leetcode is cool", "happy
    Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

    Given a string sentence, return true if it is circular. Otherwise, return
    false.
Link: https://leetcode.com/problems/circular-sentence/
Notes:
"""

import unittest


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        N = len(words)
        if N == 0 or words[0][0] != words[-1][-1]:
            return False
        last = words[0][-1]
        for word in words[1:]:
            if word[0] != last:
                return False
            last = word[-1]
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isCircularSentence1(self):
        s = "leetcode exercises sound delightful"
        self.assertEqual(self.sol.isCircularSentence(s), True)

    def test_isCircularSentence2(self):
        s = "eetcode"
        self.assertEqual(self.sol.isCircularSentence(s), True)

    def test_isCircularSentence3(self):
        s = "Leetcode is cool"
        self.assertEqual(self.sol.isCircularSentence(s), False)


if __name__ == '__main__':
    unittest.main()
