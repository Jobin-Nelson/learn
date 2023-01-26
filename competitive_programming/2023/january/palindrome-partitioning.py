'''
Created Date: 2023-01-22
Qn: Given a string s, partition s such that every substring of the partition is
    a palindrome . Return all possible palindrome partitioning of s.
Link: https://leetcode.com/problems/palindrome-partitioning/
Notes:
    - use backtracking
    - helper function to determine if it is palindrome
'''
def partition(s: str) -> list[list[str]]:
    def is_palindrom(s: str) -> bool:
        return s == s[::-1]

    def backtrack(start: int, path: list[str]):
        if start == len(s):
            res.append(path)
            return

        for i in range(start, len(s)):
            if is_palindrom(s[start:i+1]):
                backtrack(i+1, path + [s[start:i+1]])
    res = []
    backtrack(0, [])
    return res

if __name__ == '__main__':
    s1 = "aab"
    s2 = "a"

    print(partition(s1))
    print(partition(s2))
