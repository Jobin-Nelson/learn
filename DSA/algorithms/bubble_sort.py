def bubble_sort(arr):
    size = len(arr)

    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break

def bubble_sort_table(table, key):
    size = len(table)

    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if table[i][key] > table[i+1][key]:
                table[i][key], table[i+1][key] = table[i+1][key], table[i][key]
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    arr = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(arr)
    print(arr)

    table = [
            {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
            {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
            {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-8'}
            ]
    bubble_sort_table(table, 'transaction_amount')
    print(table)
