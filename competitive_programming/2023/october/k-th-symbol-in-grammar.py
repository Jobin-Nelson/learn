'''
Created Date: 2023-10-25
Qn: We build a table of n rows (1-indexed). We start by writing 0 in the 1st
    row. Now in every subsequent row, we look at the previous row and replace
    each occurrence of 0 with 01, and each occurrence of 1 with 10.

        For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the
        3rd row is 0110.

    Given two integer n and k, return the kth (1-indexed) symbol in the nth row
    of a table of n rows.
Link: https://leetcode.com/problems/k-th-symbol-in-grammar/
Notes:
    - use binary search to find the kth symbol
'''
def kthGrammar(n: int, k: int) -> int:
    cur = 0
    l, r = 1, 2**(n-1)

    for _ in range(n-1):
        m = (l + r) >> 1
        if k <= m:
            r = m
        else:
            l = m + 1
            cur ^= 1
    return cur

if __name__ == '__main__':
    n1, k1 = 1, 1
    n2, k2 = 2, 1
    n3, k3 = 2, 2

    print(kthGrammar(n1, k1))
    print(kthGrammar(n2, k2))
    print(kthGrammar(n3, k3))
