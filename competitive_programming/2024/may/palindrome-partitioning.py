"""
Created Date: 2024-05-22
Qn: Given a string s, partition s such that every
    substring of the partition is a palindrome . Return all possible palindrome
    partitioning of s.
Link: https://leetcode.com/problems/palindrome-partitioning/
Notes:
    - use dfs
"""
def partition(s: str) -> list[list[str]]:
    res = []
    part = []
    def is_palindrome(l: int, r: int) -> bool:
        cur_s = s[l:r+1]
        return all(cur_s[i] == cur_s[r-l-i] for i in range(r-l+1))

    def dfs(i: int):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()
    dfs(0)
    return res

if __name__ == '__main__':
    s1 = "aab"
    s2 = "a"

    print(partition(s1))
    print(partition(s2))
