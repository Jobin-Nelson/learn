def turbo_sort(input_str):
    ls = list(input_str)

    i = 0
    while i < len(ls):
        if i > 0:
            index = i
            larger = ls[index]
            largest = ls[i-1]
            found = False
            for idx, ch in enumerate(ls[i:], i):
                if ch > larger and ch < largest:
                    larger = ch
                    index = idx
                    found = True
            if not found and i+1 < len(ls): 
                # if no character was found satisfying the condition 
                # reset with the largest character on the next index
                i += 1
                index = find_largest(ls[i:], i)
        else:  
            index = find_largest(ls, 0)  # for the zeroth index

        ls[i], ls[index] = ls[index], ls[i]
        i += 1

    return ''.join(ls)

def find_largest(arr, ind):  # helper function
    index = 0
    largest = arr[index]
    for idx, ch in enumerate(arr, ind):
        if ch > largest:
            largest = ch
            index = idx
    return index or ind  # if index is 0 returns ind

if __name__ == '__main__':
    input_str1 = 'turbolab'
    input_str2 = 'haihai'
    output1 = turbo_sort(input_str1)
    output2 = turbo_sort(input_str2)
    print(output1)
    print(output2)