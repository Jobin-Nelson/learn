def count_rotation(nums):
    l, r = 0, len(nums)-1

    while l <= r:
        m = (r + l) // 2
        print('middle number is: ', nums[m])
        
        if m > 0 and nums[m-1] > nums[m]:
            return m
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return 0
if __name__ == '__main__':
    nums = [5, 6, 7, 1, 2, 3, 4]
    nums2 = [5, 6, 7, 8, 2, 3, 4]
    nums3 = [5, 6, 0, 1, 2, 3, 4]
    nums4 = [5, 6, 7, 8, 9, 3, 4]
    nums5 = [5, -1, 0, 1, 2, 3, 4]
    print(count_rotation(nums))
    print(count_rotation(nums2))
    print(count_rotation(nums3))
    print(count_rotation(nums4))
    print(count_rotation(nums5))
