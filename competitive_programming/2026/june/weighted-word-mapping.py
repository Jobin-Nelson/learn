"""
Created Date: 2026-06-13
Qn: You are given an array of strings words, where each string represents a
    word containing lowercase English letters.

    You are also given an integer array weights of length 26, where weights[i]
    represents the weight of the ith lowercase English letter.

    The weight of a word is defined as the sum of the weights of its
    characters.

    For each word, take its weight modulo 26 and map the result to a lowercase
    English letter using reverse alphabetical order (0 -> 'z', 1 -> 'y', ...,
    25 -> 'a').

    Return a string formed by concatenating the mapped characters for all words
    in order.
Link: https://leetcode.com/problems/weighted-word-mapping/
Notes:
"""

import unittest


class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ord_a = ord('a')
        ord_z = ord('z')

        def char_to_weight(char: str) -> int:
            return weights[ord(char) - ord_a]

        def weight_to_char(weight: int) -> str:
            return chr(ord_z - (weight % 26))

        def word_to_char(word: str) -> str:
            total_weight = sum((char_to_weight(c) for c in word), 0)
            return weight_to_char(total_weight)

        return ''.join(map(word_to_char, words))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        words = ["abcd", "def", "xyz"]
        weights = [
            5,
            3,
            12,
            14,
            1,
            2,
            3,
            2,
            10,
            6,
            6,
            9,
            7,
            8,
            7,
            10,
            8,
            9,
            6,
            9,
            9,
            8,
            3,
            7,
            7,
            2,
        ]
        expected = "rij"
        self.assertEqual(expected, self.sol.mapWordWeights(words, weights))

    def test2(self):
        words = ["a", "b", "c"]
        weights = [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ]
        expected = "yyy"
        self.assertEqual(expected, self.sol.mapWordWeights(words, weights))

    def test3(self):
        words = ["abcd"]
        weights = [
            7,
            5,
            3,
            4,
            3,
            5,
            4,
            9,
            4,
            2,
            2,
            7,
            10,
            2,
            5,
            10,
            6,
            1,
            2,
            2,
            4,
            1,
            3,
            4,
            4,
            5,
        ]
        expected = "g"
        self.assertEqual(expected, self.sol.mapWordWeights(words, weights))


if __name__ == '__main__':
    unittest.main()
