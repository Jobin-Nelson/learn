'''
Qn: Given an array nums. We define a running sum of an array as 
    runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Notes:
- add cumulative sum inplace and return the list
'''
def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

if __name__ == '__main__':
    n1 = [1,2,3,4]
    n2 = [1,1,1,1,1]
    n3 = [3,1,2,10,1]
    print(runningSum(n1))
    print(runningSum(n2))
    print(runningSum(n3))
