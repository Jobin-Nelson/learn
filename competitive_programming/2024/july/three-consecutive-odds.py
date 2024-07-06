"""
Created Date: 2024-07-01
Qn: Given an integer array arr, return true if there are three consecutive odd
    numbers in the array. Otherwise, return false. 
Link: https://leetcode.com/problems/three-consecutive-odds/
Notes:
"""
def threeConsecutiveOdds(arr: list[int]) -> bool:
    odd = 0
    for n in arr:
        if n & 1:
            odd += 1
        else:
            odd = 0
        if odd == 3:
            return True
    return False

if __name__ == '__main__':
    a1 = [2,6,4,1]
    a2 = [1,2,34,3,4,5,7,23,12]

    print(threeConsecutiveOdds(a1))
    print(threeConsecutiveOdds(a2))
