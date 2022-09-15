'''
Created Date: 30-06-2022
Qn: Given an integer array nums of size n, return the minimum number of moves 
    required to make all array elements equal.
    In one move, you can increment or decrement an element of the array by 1.
    Test cases are designed so that the answer will fit in a 32-bit integer.
Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
Notes:
    - sort the array find sum of deviation with median
'''
def minMoves2(nums: list[int]) -> int:
    nums.sort()
    median = nums[len(nums)//2]
    return sum(abs(median - n) for n in nums)

if __name__ == '__main__':
    n1 = [1, 2, 3]
    n2 = [1, 10, 2, 9]
    print(minMoves2(n1))
    print(minMoves2(n2))
