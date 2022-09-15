'''
Created Date: 2022-08-30
Qn: You are given an n x n 2D matrix representing an image, rotate the image by
    90 degrees (clockwise). You have to rotate the image in-place, which means you
    have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix
    and do the rotation. 
Link: https://leetcode.com/problems/rotate-image/
Notes:
    - store top left value in a variable and rotate each element of the outer square 
    - recursively rotate inward
'''
from pprint import pprint

def rotate(matrix: list[list[int]]) -> None:
    l, r = 0, len(matrix[0]) - 1

    while l < r:
        for i in range(r - l):
            t, b = l, r

            top_left = matrix[t][l + i]

            matrix[t][l + i] = matrix[b - i][l]

            matrix[b - i][l] = matrix[b][r - i]

            matrix[b][r - i] = matrix[t + i][r]

            matrix[t + i][r] = top_left

        r -= 1
        l += 1

    
if __name__ == '__main__':
    m1 =  [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(m1)
    rotate(m2)
    pprint(m1)
    pprint(m2)
