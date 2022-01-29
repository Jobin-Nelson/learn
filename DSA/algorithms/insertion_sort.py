def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # making a copy of the current element since the position would be filled by the previous element
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] # shifting the elements forward making space for the current element
            j -= 1

        arr[j+1] = key # inserting the saved current element in the right sorted position

    return arr

if __name__ == '__main__':
    print(insertion_sort([9, 2, 5, 4, 9, 8]))
    print(insertion_sort([1, 2, 5, 4, 9, 8]))
