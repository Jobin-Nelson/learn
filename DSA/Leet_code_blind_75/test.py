def merge(list):
    m = len(list) // 2
    l, r = list[:m], list[m:]
    merge(l)
    merge(r)

    i, j, k = 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            list[k] = l[i]
            i += 1
        else:
            list[k] = r[j]
            j += 1
        k += 1
    
    while i < len(l):
        list[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        list[k] = r[j]
        j += 1
        k += 1

