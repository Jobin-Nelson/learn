"""
Created Date: 2024-03-02
Qn: Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Notes:
"""
def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(map(lambda x: x*x, nums))

if __name__ == '__main__':
    n1 = [-4,-1,0,3,10]
    n2 = [-7,-3,2,3,11]

    print(sortedSquares(n1))
    print(sortedSquares(n2))
