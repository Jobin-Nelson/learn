# Given a sorted array of integers arr and an integer target, find the index of the first and last position of target in arr.
# If target can't be found in arr, return [-1, -1]

# binary search twice for finding start and end
def find_start(arr, target):
    if arr[0] == target:
        return 0

    l, r = 0, len(arr)-1

    while l<=r:
        m = (l + r)//2
        if (arr[m] == target) and (arr[m-1] < target):
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


def find_end(arr, target):
    if arr[-1] == target:
        return len(arr)-1

    l, r = 0, len(arr)-1

    while l<=r:
        m = (l + r)//2
        if (arr[m] == target) and (arr[m+1] > target):
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

def first_and_last(arr, target):
    if (len(arr) == 0) or (arr[0] > target) or (arr[-1] < target):
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]
