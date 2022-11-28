'''
Created Date: 22-06-2022
Qn: Given an integer array nums and an integer k, return the kth largest 
    element in the array. Note that it is the kth largest element in the 
    sorted order, not the kth distinct element.
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Notes:
    - sort and return len - kth, time complexity O(nlogn)
    - quickselect for average time complexity of O(n), worst case O(n^2)
'''
def findKthLargest(nums: list[int], k: int) -> int:
    # return sorted(nums)[-k]

    k = len(nums) - k

    def quickSelect(l, r):
        nonlocal k
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p < k: return quickSelect(p+1, r)
        elif p > k: return quickSelect(l, p - 1)
        else: return nums[p]
    return quickSelect(0, len(nums) - 1)

if __name__ == '__main__':
    n1, k1 = [3, 2, 1, 5, 6, 4], 2
    n2, k2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    print(findKthLargest(n1, k1))
    print(findKthLargest(n2, k2))
