def max_area(nums):
    area = 0
    l, r = 0, len(nums) -1 
    while l < r:
        cur_area = (r - l) * min(nums[l], nums[r])
        area = max(area, cur_area)

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return area
if __name__ == '__main__':
    height1 = [1, 1]
    height2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height1))
    print(max_area(height2))
