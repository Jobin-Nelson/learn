def binary_search(list, target):
    l, r = 0, len(list)-1

    while l<=r:
        m = (l + r)//2
        if list[m] == target:
            if m-1 >= 0 and list[m-1] == target:
                r = m - 1
            else:
                return m
        elif list[m] < target:
            l = m + 1
        else:
            r = m - 1
        
    return None

def verify(index):
    if index:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')

def recursive_binary_search(list, target):
    if len(list) ==0:
        return False
    else:
        m = len(list)//2

        if list[m] == target:
            return True
        else:
            if list[m] < target:
                return recursive_binary_search(list[m+1:], target)
            else:
                return recursive_binary_search(list[:m], target)

def verify_rec(result):
    print('Target found: ', result)


if __name__ == '__main__':
    print('Binary search')
    numbers = [1, 2, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 11]
    verify(binary_search(numbers, 7))

    print('Recursive binary search to check if the target is in the list')
    verify_rec(recursive_binary_search(numbers, 7))

