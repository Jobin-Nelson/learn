'''
Created Date: 2023-11-22
Qn: Given a 2D integer array nums, return all elements of nums in diagonal
    order as shown in the below images.
Link: https://leetcode.com/problems/diagonal-traverse-ii/
Notes:
    - use queue to traverse diagonally
    - if c == 0 append the cell below
    - append the cell to the right
'''
from collections import deque

def findDiagonalOrder(nums: list[list[int]]) -> list[int]:
    q = deque([(0, 0)])
    res = []
    while q:
        r, c = q.popleft()
        res.append(nums[r][c])
        if c == 0 and r + 1 < len(nums):
            q.append((r+1, c))
        if c+1 < len(nums[r]):
            q.append((r, c+1))
    return res


    # M, N = len(nums), max(len(v) for v in nums)
    # res = []
    # ci = cj = 0
    # while True:
    #     i = ci
    #     j = cj
    #     if ci == M-1:
    #         if cj == N: break
    #         cj += 1
    #     else:
    #         ci += 1
    #     while i >= 0:
    #         if j < len(nums[i]): res.append(nums[i][j])
    #         i -= 1
    #         j += 1
    # return res

if __name__ == '__main__':
    n1 = [[1,2,3],[4,5,6],[7,8,9]]
    n2 = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    n3 = [[14,12,19,16,9],
          [13,14,15,8,11],
          [11,13,1]]

    print(findDiagonalOrder(n1))
    print(findDiagonalOrder(n2))
    print(findDiagonalOrder(n3))
