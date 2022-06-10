'''
Created Date: 05-06-2022
Qn: The n-queens puzzle is the problem of placing n queens on an n x n 
    chessboard such that no two queens attack each other.
    Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Link: https://leetcode.com/problems/n-queens-ii/
Notes:
- backtracking
'''
def totalNQueens(n: int) -> int:
    res = 0

    def dfs(row, ex):
        nonlocal res
        if row < n:
            for col in range(n):
                if (row, col) in ex: continue
                ex_sub = set()
                r1 = r2 = r3 = row
                c1 = c2 = c3 = col

                while r1 < n:
                    r1 += 1
                    ex_sub.add((r1, c1))
                while c2 < n:
                    c2 += 1
                    r2 += 1
                    ex_sub.add((r2, c2))
                while c3 > 0:
                    c3 -= 1
                    r3 += 1
                    ex_sub.add((r3, c3))
                dfs(row+1, ex | ex_sub)
        else:
            res += 1
    dfs(0, set())
    return res

if __name__ == '__main__':
    n1, n2 = 4, 1
    print(totalNQueens(n1))
    print(totalNQueens(n2))
