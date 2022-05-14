def merge_sort(arr):
    '''
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    ''' 
    if len(arr) > 1:
        m = len(arr) // 2
        l, r = arr[:m], arr[m:]

        merge_sort(l) # recurses till it hits a single element
        merge_sort(r)

        i, j, k = 0, 0, 0

        while i < len(l) and j < len(r): # merges the two lists (l, r) while sorting them 
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
