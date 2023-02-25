'''
Created Date: 2023-02-20
Qn: Given a sorted array of distinct integers and a target value, return the
    index if the target is found. If not, return the index where it would be if
    it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
Link: https://leetcode.com/problems/search-insert-position/
Notes:
    - use binary search
'''
def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (r + l) >> 1
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return l

if __name__ == '__main__':
    n1, t1 = [1,3,5,6], 5
    n2, t2 = [1,3,5,6], 2
    n3, t3 = [1,3,5,6], 7

    print(searchInsert(n1, t1))
    print(searchInsert(n2, t2))
    print(searchInsert(n3, t3))
