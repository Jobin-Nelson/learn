'''
Created Date: 2023-09-28
Qn: Given an integer array nums, move all the even integers at the beginning of
    the array followed by all the odd integers.

    Return any array that satisfies this condition.
Link: https://leetcode.com/problems/sort-array-by-parity/
Notes:
'''
def sortArrayByParity(nums: list[int]) -> list[int]:
    # return sorted(nums, key=lambda x: x & 1)
    res, odd = [], []
    for num in nums:
        if num & 1:
            odd.append(num)
        else:
            res.append(num)
    res.extend(odd)
    return res

if __name__ == '__main__':
    n1 = [3,1,2,4]
    n2 = [0]

    print(sortArrayByParity(n1))
    print(sortArrayByParity(n2))
