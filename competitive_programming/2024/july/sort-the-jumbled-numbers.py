"""
Created Date: 2024-07-24
Qn: You are given a 0-indexed integer array mapping which
    represents the mapping rule of a shuffled decimal system.
    mapping[i] = j means digit i should be mapped to digit j in
    this system.

    The mapped value of an integer is the new integer obtained
    by replacing each occurrence of digit i in the integer with
    mapping[i] for all 0 <= i <= 9.

    You are also given another integer array nums. Return the
    array nums sorted in non-decreasing order based on the
    mapped values of its elements.

    Notes:

        - Elements with the same mapped values should appear in
          the same relative order as in the input.
        - The elements of nums should only be sorted based on
          their mapped values and not be replaced by them.
Link: https://leetcode.com/problems/sort-the-jumbled-numbers/
    - use sorting 
"""
def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
    mapped_nums = [0] * len(nums)

    for i, n in enumerate(nums):
        cur = n
        num = 0
        place = 1
        if cur == 0:
            mapped_nums[i] = mapping[0]
            continue
        while cur:
            num = place * mapping[cur % 10] + num
            cur //= 10
            place *= 10
        mapped_nums[i] = num

    sorted_indices = sorted(range(len(nums)), key=lambda i: (mapped_nums[i], i))
    return [nums[i] for i in sorted_indices]

if __name__ == '__main__':
    m1, n1 = [8,9,4,0,2,1,3,5,7,6], [991,338,38]
    m2, n2 = [0,1,2,3,4,5,6,7,8,9], [789, 456,123]
    m3, n3 = [9,8,7,6,5,4,3,2,1,0], [0,1,2,3,4,5,6,7,8,9]
    m4, n4 = [0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0]

    print(sortJumbled(m1, n1))
    print(sortJumbled(m2, n2))
    print(sortJumbled(m3, n3))
    print(sortJumbled(m4, n4))
