'''
Created Date: 2023-02-06
Qn: Given the array nums consisting of 2n elements in the form
    [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
Link: https://leetcode.com/problems/shuffle-the-array/
Notes:
    - use two pointers
'''
def shuffle(nums: list[int], n: int) -> list[int]:
    res = []

    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])

    return res

if __name__ == '__main__':
    nums1, n1 = [2,5,1,3,4,7], 3
    nums2, n2 = [1,2,3,4,4,3,2,1], 4
    nums3, n3 = [1,1,2,2], 2

    print(shuffle(nums1, n1))
    print(shuffle(nums2, n2))
    print(shuffle(nums3, n3))
