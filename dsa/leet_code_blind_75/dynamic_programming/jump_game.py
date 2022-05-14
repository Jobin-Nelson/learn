'''
Qn: You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Link: https://leetcode.com/problems/jump-game/
Notes:
- bottom up approach traversing through the entire nums array and return true if the variable is 0 else false
'''
# greedy
def can_jump(nums):
    goal = len(nums) -1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False

if __name__ == '__main__':
    n1, n2 = [2, 3, 1, 1, 4], [3, 2, 1, 0, 4]
    print(can_jump(n1))
    print(can_jump(n2))
