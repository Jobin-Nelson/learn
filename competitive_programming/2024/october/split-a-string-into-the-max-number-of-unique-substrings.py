"""
Created Date: 2024-10-21
Qn: Given a string s, return the maximum number of unique substrings that the
    given string can be split into.

    You can split string s into any list of non-empty substrings, where the
    concatenation of the substrings forms the original string. However, you
    must split the substrings such that all of them are unique.

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
Notes:
    - use backtracking
"""
def maxUniqueSplit(s: str) -> int:
    def dfs(i: int, cur_set: set[str]) -> int:
        if i == len(s):
            return 0
        res = 0
        for j in range(i, len(s)):
            sl = s[i:j+1]
            if sl in cur_set:
                continue
            cur_set.add(sl)
            res = max(res, dfs(j+1, cur_set) + 1)
            cur_set.remove(sl)
        return res
    return dfs(0, set())
    # store = set()
    # N = len(s)
    # res = []
    # l, r = 0, 0
    # while r < N:
    #     sl = s[l:r+1]
    #     if sl not in store:
    #         res.append(sl)
    #         store.add(sl)
    #         l = r+1
    #     r += 1
    # print(res)
    # return len(res)

if __name__ == '__main__':
    s1 = "ababccc"
    s2 = "aba"
    s3 = "aa"

    print(maxUniqueSplit(s1))
    print(maxUniqueSplit(s2))
    print(maxUniqueSplit(s3))
