"""
Created Date: 2024-01-23
Qn: You are given an array of strings arr. A string s is formed by the
    concatenation of a subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Notes:
    - use bitmask and backtracking
"""
def maxLength(arr: list[str]) -> int:
    # backtracking
    # chars = set()
    # def overlap(charset1: set[str], s2: str) -> bool:
    #     charset2 = set(s2)
    #     return len(charset1) + len(charset2) != len(charset1 | charset2)
    #
    # def backtrack(i: int) -> int:
    #     if i == len(arr): return len(chars)
    #     res = 0
    #     if not overlap(chars, arr[i]):
    #         for c in arr[i]:
    #             chars.add(c)
    #         res = backtrack(i+1)
    #         for c in arr[i]:
    #             chars.remove(c)
    #     return max(res, backtrack(i+1))
    # return backtrack(0)
    
    # bitmask
    chars = 0
    zero_val = ord('a')
    def backtrack(i: int, chars: int) -> int:
        if i == len(arr): return chars.bit_count()
        new_chars = chars
        valid_string = True
        res = 0
        for a in arr[i]:
            bit = 1 << (ord(a) - zero_val)
            if new_chars & bit == 0:
                new_chars |= bit
            else:
                valid_string = False
                break
        if valid_string:
            res = backtrack(i+1, new_chars)
        return max(res, backtrack(i+1, chars))
    return backtrack(0, chars)

        

if __name__ == '__main__':
    a1 = ["un", "iq", "ue"]
    a2 = ["cha","r","act","ers"] 
    a3 = ["abcdefghijklmnopqrstuvwxyz"]

    print(maxLength(a1))
    print(maxLength(a2))
    print(maxLength(a3))
