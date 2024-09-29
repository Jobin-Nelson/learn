"""
Created Date: 2024-09-29
Qn: Design a data structure to store the strings' count with the ability to
    return the strings with minimum and maximum counts.

    Implement the AllOne class:

    - AllOne() Initializes the object of the data structure.
    - inc(String key) Increments the count of the string key by 1. If key does
      not exist in the data structure, insert it with count 1.
    - dec(String key) Decrements the count of the string key by 1. If the count
      of key is 0 after the decrement, remove it from the data structure. It is
      guaranteed that key exists in the data structure before the decrement.
    - getMaxKey() Returns one of the keys with the maximal count. If no element
      exists, return an empty string "".
    - getMinKey() Returns one of the keys with the minimum count. If no element
      exists, return an empty string "". Note that each function must run in
      O(1) average time complexity.
Link: https://leetcode.com/problems/all-oone-data-structure/
Notes:
"""
# from functools import reduce, partial
# from operator import mul, add
# from typing import Callable
#
# identity = lambda x: x
# def compose(*f: Callable) -> Callable:
#     def inner(f: Callable, g: Callable) -> Callable:
#         return lambda x: f(g(x))
#     return reduce(inner, f, identity)
#
# def curried_mod(mod: int) -> Callable:
#     def inner(val: int) -> int:
#         return val % mod
#     return inner
#
# big_prime = 10 ** 9 + 7
# mul_10 = partial(mul, 10)
# mod_big_prime = curried_mod(big_prime)
# mul_10_mod_big_prime = compose(mod_big_prime, mul_10)
# hash = lambda x: reduce(lambda y, z: mul_10_mod_big_prime(y+z), x, identity)

from sys import maxsize

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class AllOne:
    def __init__(self):
        self.root = TrieNode()
        self.min = maxsize
        self.max = 0
    def build_trie(self, word: str):
        cur = self.root
        ord_a = ord('a')
        for c in word:
            ind = ord(c) - ord_a
            if cur.children[ind] is None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
            cur.count += 1
            self.max()
    def inc(self, key: str) -> None:

    def dec(self, key: str) -> None:
        pass
    def getMaxKey(self) -> str:
        pass
    def getMinKey(self) -> str:
        pass

raise ValueError('Unfinished Question')

if __name__ == '__main__':
    ao1 = AllOne()
    print(ao1.inc('hello'))
    print(ao1.inc('hello'))
    print(ao1.getMaxKey())
    print(ao1.getMinKey())
    print(ao1.inc('leet'))
    print(ao1.getMaxKey())
    print(ao1.getMinKey())
