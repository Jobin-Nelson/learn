def hoare_partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    start = pivot_index + 1
    end = len(arr) -1

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end

def recurse(arr, start, end):
    if start < end:
        pi = hoare_partition(arr, start, end)
        recurse(arr, start, pi -1)
        recurse(arr, pi + 1, end)

def quick_sort(arr):
    start, end = 0, len(arr) - 1
    recurse(arr, start, end)

if __name__ == '__main__':
    ls = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(ls)
    print(ls)
