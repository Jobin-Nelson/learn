'''
Created Date: 2023-08-07
Qn: You are given an m x n integer matrix matrix with the following two properties:

        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer of the
          previous row.

    Given an integer target, return true if target is in matrix or false
    otherwise.

    You must write a solution in O(log(m * n)) time complexity.
Link: https://leetcode.com/problems/search-a-2d-matrix/
Notes:
    - use binary search
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    l, r = 0, len(matrix[0]) - 1
    for m in matrix:
        l, r = 0, len(matrix[0]) - 1
        if target < m[l]: break
        if target > m[r]: continue
        while l <= r:
            mid = (l + r) >> 1
            if m[mid] == target: return True
            if m[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    return False

if __name__ == '__main__':
    m1, t1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
    m2 ,t2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
    m3, t3 = [[1]], 1

    print(searchMatrix(m1, t1))
    print(searchMatrix(m2, t2))
    print(searchMatrix(m3, t3))
