'''
Created Date: 09-06-2022
Qn: Given a 1-indexed array of integers numbers that is already sorted in 
    non-decreasing order, find two numbers such that they add up to a specific 
    target number. Let these two numbers be numbers[index1] and numbers[index2] 
    where 1 <= index1 < index2 <= numbers.length. Return the indices of the two 
    numbers, index1 and index2, added by one as an integer array [index1, index2] 
    of length 2.
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Notes:
- two pointer one at each end, move end when sum is larger and vice versa
'''
def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        cur_sum = numbers[l] + numbers[r]
        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return -1

if __name__ == '__main__':
    n1, t1 = [2, 7, 11, 15], 9
    n2, t2 = [2, 3, 4], 6
    n3, t3 = [-1, 0], -1
    print(twoSum(n1, t1))
    print(twoSum(n2, t2))
    print(twoSum(n3, t3))
