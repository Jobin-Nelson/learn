"""
Created Date: 2024-07-25
Qn: Given an array of integers nums, sort the array in ascending order and
    return it.

    You must solve the problem without using any built-in functions in
    O(nlog(n)) time complexity and with the smallest space complexity
    possible.
Link: https://leetcode.com/problems/sort-an-array/
Notes:
    - use merge sort
"""


def sortArray(nums: list[int]) -> list[int]:
    def merge(arr: list[int], l: int, r: int) -> list[int]:
        if l == r:
            return arr

        m = l + ((r - l) >> 1)
        merge(arr, l, m)
        merge(arr, m + 1, r)

        left = arr[l : m + 1]
        right = arr[m + 1 : r + 1]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        return arr

    return merge(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    n1 = [5, 2, 3, 1]
    n2 = [5, 1, 1, 2, 0, 0]

    print(sortArray(n1))
    print(sortArray(n2))
