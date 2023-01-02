'''
Created Date: 2022-12-26
Qn: You are given an integer array nums. You are initially positioned at the
    array's first index, and each element in the array represents your maximum
    jump length at that position.

    Return true if you can reach the last index, or false otherwise.
Link: https://leetcode.com/problems/jump-game/
Notes:
    - set goal as len of nums
    - iterate backwards and reset goal to i if i + nums[i] >= goal
    - check goal is 0
'''
def canJump(nums: list[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums)-1, -1, -1):
        if (i + nums[i]) >= goal: goal = i
    return goal == 0

if __name__ == '__main__':
    n1 = [2,3,1,1,4]
    n2 = [3,2,1,0,4]

    print(canJump(n1))
    print(canJump(n2))
