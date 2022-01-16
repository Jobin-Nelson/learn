# find the kth largest integer from the array

# removing maximum k-1 times
def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

# sorted and returning kth element starting from the end
def kth_sort_larget(arr, k):
    arr.sort()
    return arr[-k]

# with heap
import heapq

def kth_heap_largest(arr, k):
    arr = [-el for el in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
