def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l, r = arr[:m], arr[m:]

        merge_sort(l)
        merge_sort(r)

        i, j, k = 0, 0, 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

if __name__ == '__main__':
    arr = [3, 5, 2, 7, 4, 7, 6, ]
    print(arr)
    merge_sort(arr)
    print(arr)
