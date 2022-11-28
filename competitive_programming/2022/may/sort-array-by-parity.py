'''
Qn: Given an integer array nums, move all the even integers at the beginning 
    of the array followed by all the odd integers.
Link: https://leetcode.com/problems/sort-array-by-parity/
Notes:
    - use two lists to track even and odd, return concatenated list
    - use two pointers and swap from first to last
'''
def sort_array_by_parity(nums: list[list[int]]) -> list[int]:
    even, odd = [], []
    for n in nums:
        if n % 2:
            odd.append(n)
        else:
            even.append(n)
    return even + odd

def sort_array_by_parity_two_pointer(nums: list[list[int]]) -> list[int]:
    i, j = 0, len(nums)-1

    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] % 2 == 0: i += 1
        if nums[j] % 2 == 1: j -= 1
    return nums

if __name__ == '__main__':
    n1, n2 = [3,1,2,4], [0]
    print(sort_array_by_parity(n1))
    print(sort_array_by_parity(n2))

    print(sort_array_by_parity_two_pointer(n1))
    print(sort_array_by_parity_two_pointer(n2))
