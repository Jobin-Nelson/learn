'''
Created Date: 2022-09-18
Qn: Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.
Link: https://leetcode.com/problems/trapping-rain-water/
Notes:
    - two pointer at two opposite ends
    - push the minimum pointer forward
    - keep track the of max_l & max_r
    - reduce from respective max_pointer the current height and add the result
'''
def trap(height: list[int]) -> int:
    if not height: return 0
    total_area = 0
    l, r = 0, len(height)-1
    max_l, max_r = height[l], height[r]

    while l < r:
        if max_l < max_r:
            l += 1
            max_l = max(max_l, height[l])
            total_area += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            total_area += max_r - height[r]
    return total_area


if __name__ == '__main__':
    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    h2 = [4, 2, 0, 3, 2, 5]

    print(trap(h1))
    print(trap(h2))
