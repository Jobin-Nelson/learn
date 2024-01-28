"""
Created Date: 2024-01-22
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
    - use counter, inplace, or math approach
"""
def findErrorNums(nums: list[int]) -> list[int]:
    # hashmap approach
    # c = Counter(nums)
    # return [next(filter(lambda x: c[x] == 2, c)), next(filter(lambda x: c[x] == 0, range(1, len(nums)+1)))]

    # inplace approach
    # res = [0, 0]
    # for n in nums:
    #     n = abs(n)
    #     nums[n-1] *= -1
    #     if nums[n-1] > 0:
    #         res[0] = n
    # for i, n in enumerate(nums):
    #     if n > 0 and i+1 != res[0]:
    #         res[1] = i + 1
    # return res

    # math approach
    x = 0 # duplicate - missing
    y = 0 # duplicate^2 - missing^2

    for i in range(1, len(nums)+1):
        x += nums[i-1] - i
        y += nums[i-1]**2 - i**2

    missing = (y-x**2) // (2 * x)
    duplicate = missing + x
    return [duplicate, missing]


if __name__ == '__main__':
    n1 = [1,2,2,4]
    n2 = [1,1]

    print(findErrorNums(n1))
    print(findErrorNums(n2))
