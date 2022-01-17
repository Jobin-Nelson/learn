def merge_sort(list):
    '''
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    ''' 
    if len(list) <= 1:
        return list

    l, r = split(list)

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)

def split(list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - l and r
    '''
    m = len(list)//2

    l, r = list[:m], list[m:]

    return l, r

def merge(l, r):
    '''
    Merges two lists, sorting them in the process
    Returns a new merged list
    '''
    ls = []
    i = 0
    j = 0
    
    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            ls.append(l[i])
            i += 1
        else:
            ls.append(r[j])
            j += 1

    while i < len(l):
        ls.append(l[i])
        i += 1

    while j < len(r):
        ls.append(r[j])
        j += 1

    return ls

if __name__ == '__main__':
    alist = [43, 23, 54, 68, 72, 88, 91]

    sorted_list = merge_sort(alist)

    print(sorted_list)
