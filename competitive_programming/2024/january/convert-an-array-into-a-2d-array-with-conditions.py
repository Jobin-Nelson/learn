"""
Created Date: 2024-01-02
Qn: You are given an integer array nums. You need to create a 2D array from
    nums satisfying the following conditions:

        - The 2D array should contain only the elements of the array nums. 
        - Each row in the 2D array contains distinct integers. 
        - The number of rows in the 2D array should be minimal.

    Return the resulting array. If there are multiple answers, return any of
    them.

    Note that the 2D array can have a different number of elements on each row.
Link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
Notes:
    - use counter and create rows
"""
from collections import Counter

def findMatrix(nums: list[int]) -> list[list[int]]:
    res = []
    counter = Counter(nums)
    while True:
        cur_row = []
        for k, v in counter.items():
            if v == 0: continue
            counter[k] = v - 1
            cur_row.append(k)
        if len(cur_row) == 0: break
        res.append(cur_row)
    return res

if __name__ == '__main__':
    n1 = [1,3,4,1,2,3,1]
    n2 = [1,2,3,4]

    print(findMatrix(n1))
    print(findMatrix(n2))
