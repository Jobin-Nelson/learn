'''
Created Date: 2022-10-23
Qn: You have a set of integers s, which originally contains all the numbers
    from 1 to n. Unfortunately, due to some error, one of the numbers in s got
    duplicated to another number in the set, which results in repetition of one
    number and loss of another number.

    You are given an integer array nums representing the data status of this
    set after the error.

    Find the number that occurs twice and the number that is missing and return
    them in the form of an array.
Link: https://leetcode.com/problems/set-mismatch/
Notes:
    - pure maths
'''
def findErrorNums(nums: list[int]) -> list[int]:
    N = len(nums)
    given_sum = sum(set(nums))
    actual_sum = N * (N + 1) // 2
    a = actual_sum - given_sum
    b = sum(nums) - actual_sum + a
    return [b, a]

if __name__ == '__main__':
    n1 = [1, 2, 2, 4]
    n2 = [1, 1]

    print(findErrorNums(n1))
    print(findErrorNums(n2))
