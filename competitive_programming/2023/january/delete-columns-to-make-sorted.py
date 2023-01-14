'''
Created Date: 2023-01-03
Qn: You are given an array of n strings strs, all of the same length.

    The strings can be arranged such that there is one on each line, making a
    grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

        abc
        bce
        cae

    You want to delete the columns that are not sorted lexicographically. In the
    above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are
    sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

    Return the number of columns that you will delete.
Link: https://leetcode.com/problems/delete-columns-to-make-sorted/
Notes:
    - inverse the matrix
    - check each row if it is lexicographically ordered
'''
def minDeletionSize(strs: list[str]) -> int:
    return sum(any(strs[i][j] < strs[i-1][j] for i in range(1, len(strs))) for j in range(len(strs[0])))

if __name__ == '__main__':
    s1 = ["cba","daf","ghi"]
    s2 = ["a","b"]
    s3 = ["zyx","wvu","tsr"]

    print(minDeletionSize(s1))
    print(minDeletionSize(s2))
    print(minDeletionSize(s3))

