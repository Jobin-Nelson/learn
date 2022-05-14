'''
Qn: Return the maximum amount of water a containter can store
Link: https://leetcode.com/problems/container-with-most-water/
Notes:
- two pointer and tracking the max area through iteration
'''

# Two pointer
def max_area(height):
    area = 0
    l, r = 0, len(height) - 1
    while l < r:
        cur_area = (r - l) * min(height[l], height[r])
        area = max(cur_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area


if __name__ == '__main__':
    height1 = [1, 1]
    height2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height1))
    print(max_area(height2))
