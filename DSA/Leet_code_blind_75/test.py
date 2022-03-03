def can_jump(nums):
    goal = len(nums) - 1
    i = len(nums) - 1
    while i >= 0:
        if i + nums[i] >= goal:
            goal = i
        i -= 1
    return not goal or False
if __name__ == '__main__':
    n1, n2 = [2, 3, 1, 1, 4], [3, 2, 1, 0, 4]
    print(can_jump(n1))
    print(can_jump(n2))

    