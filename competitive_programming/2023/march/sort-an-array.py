'''
Created Date: 2023-03-01
Qn: Given an array of integers nums, sort the array in ascending order and
    return it.

    You must solve the problem without using any built-in functions in
    O(nlog(n)) time complexity and with the smallest space complexity possible.
Link: https://leetcode.com/problems/sort-an-array/
Notes:
    - use merge sort
'''
def sortArray(nums: list[int]) -> list[int]:
    def merge_sort(nums: list[int]):
        if len(nums) < 2: return

        m = len(nums) >> 1
        l, r = nums[:m], nums[m:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1
    merge_sort(nums)
    return nums

if __name__ == '__main__':
    n1 = [5,2,3,1]
    n2 = [5,1,1,2,0,0]

    print(sortArray(n1))
    print(sortArray(n2))
