'''
Created Date: 2023-09-08
Qn: Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it as shown:
Link: https://leetcode.com/problems/pascals-triangle/
Notes:
    - can be done iteratively as well as using dfs
'''
def generate(numRows: int) -> list[list[int]]:
    res, cur = [], []
    def dfs(i: int) -> None:
        nonlocal res, cur
        if i == numRows: return
        nex = [1] * (len(cur) + 1)
        for j in range(1, len(cur)):
            nex[j] = cur[j - 1] + cur[j]
        cur = nex
        res.append(cur)
        dfs(i+1)
    dfs(0)
    return res

if __name__ == '__main__':
    n1 = 5
    n2 = 1

    print(generate(n1))
    print(generate(n2))
