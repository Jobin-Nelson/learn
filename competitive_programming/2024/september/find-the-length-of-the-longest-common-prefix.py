"""
Created Date: 2024-09-24
Qn: You are given two arrays with positive integers arr1 and arr2.

    A prefix of a positive integer is an integer formed by one or more of its
    digits, starting from its leftmost digit. For example, 123 is a prefix of
    the integer 12345, while 234 is not.

    A common prefix of two integers a and b is an integer c, such that c is a
    prefix of both a and b. For example, 5655359 and 56554 have a common prefix
    565 while 1223 and 43456 do not have a common prefix.

    You need to find the length of the longest common prefix between all pairs
    of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

    Return the length of the longest common prefix among all pairs. If no
    common prefix exists among them, return 0
Link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
Notes:
    - use trie
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 10


def build_trie(nums: list[int]) -> TrieNode:
    root = TrieNode()
    for num in map(str, nums):
        cur = root
        for d in map(int, num):
            if not cur.children[d]:
                cur.children[d] = TrieNode()
            cur = cur.children[d]
    return root


def find_longest_prefix(root: TrieNode, nums: list[int]) -> int:
    res = 0
    for num in map(str, nums):
        depth = 0
        cur = root
        for d in map(int, num):
            if cur.children[d]:
                depth += 1
                cur = cur.children[d]
            else:
                break
        res = max(res, depth)
    return res


def longestCommonPrefix(arr1: list[int], arr2: list[int]) -> int:
    trie1 = build_trie(arr1)

    return find_longest_prefix(trie1, arr2)


if __name__ == '__main__':
    a11, a12 = [1, 10, 100], [1000]
    a21, a22 = list(range(1, 4)), [4] * 3

    print(longestCommonPrefix(a11, a12))
    print(longestCommonPrefix(a21, a22))
