'''
Created Date: 2022-10-24
Qn: You are given an array of strings arr. A string s is formed by the
    concatenation of a subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Notes:
    - backtrack
    - at each string in the arr you have to two choices to make include the
      string or not
'''
def maxLength(arr: list[str]) -> int:
    char_set = set()
    N = len(arr)

    def backtrack(i):
        if i == N: return len(char_set)

        res = 0
        arr_set = set(arr[i])
        if char_set.isdisjoint(arr_set) and len(arr[i]) == len(arr_set):
            char_set.update(arr_set)
            res = backtrack(i+1)
            char_set.difference_update(arr_set)
        return max(res, backtrack(i+1))
    return backtrack(0)

if __name__ == '__main__':
    a1 = ['un', 'iq', 'ue']
    a2 = ["cha","r","act","ers"]
    a3 = ["abcdefghijklmnopqrstuvwxyz"]

    print(maxLength(a1))
    print(maxLength(a2))
    print(maxLength(a3))
