"""
Created Date: 2025-07-03
Qn: Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next
    character in the English alphabet, and append it to the original word. For
    example, performing the operation on "c" generates "cd" and performing the
    operation on "zb" generates "zbac".

    Return the value of the kth character in word, after enough operations have
    been done for word to have at least k characters.

    Note that the character 'z' can be changed to 'a' in the operation.
Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
Notes:
    - count the number of bits in k-1
"""

import unittest


class Solution:
    def kthCharacter(self, k: int) -> str:
        # Bit count
        return chr(ord('a') + (k - 1).bit_count())

        # Simulation
        # word = ['a']
        # ord_a = ord('a')
        # while len(word) < k:
        #     word.extend([chr((ord(c) - ord_a + 1 % 26) + ord_a) for c in word])
        # return word[k - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_kthCharacter1(self):
        k = 5
        expected = "b"
        self.assertEqual(expected, self.sol.kthCharacter(k))

    def test_kthCharacter2(self):
        k = 10
        expected = "c"
        self.assertEqual(expected, self.sol.kthCharacter(k))


if __name__ == '__main__':
    unittest.main()
