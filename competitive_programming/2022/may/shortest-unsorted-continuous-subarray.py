'''
Qn: Given an integer array nums, you need to find one continuous subarray 
    that if you only sort this subarray in ascending order, 
    then the whole array will be sorted in ascending order.
    Return the shortest such subarray and output its length.
Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Notes:
    - track min and max once inside the unsorted subarray
    - find the index where min and max go
'''
def find_unsorted_subarray(nums: list[int]) -> int:
    mn, mx = float('inf'), float('-inf')
    N = len(nums)
    deviated = False
    for i in range(1, N):
        if nums[i-1] > nums[i]:
            deviated = True
        if deviated:
            mn = min(mn, nums[i])

    deviated = False
    for i in range(N-2, -1, -1):
        if nums[i] > nums[i+1]:
            deviated = True
        if deviated:
            mx = max(mx, nums[i])
            
    for l in range(N):
        if nums[l] > mn:
            break
    for r in range(N-1, -1, -1):
        if nums[r] < mx:
            break
    return r-l+1 if r > l else 0

if __name__ == '__main__':
    n1, n2, n3 = [2,6,4,8,10,9,15], [1,2,3,4], [1]
    n4 = [1, 3, 2, 4, 5]
    n5 = [2,1,3,4,5]
    print(find_unsorted_subarray(n1))
    print(find_unsorted_subarray(n2))
    print(find_unsorted_subarray(n3))
    print(find_unsorted_subarray(n4))
    print(find_unsorted_subarray(n5))
