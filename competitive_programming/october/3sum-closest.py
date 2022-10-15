'''
Created Date: 2022-10-08
Qn: Given an integer array nums of length n and an integer target, find three
    integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
Link: https://leetcode.com/problems/3sum-closest/
Notes:
    - sort and two pointers
    - return sum of first three if sum is greater than target
    - return sum of last three if sum is less than target
'''
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    sums=0
    closest=sum(nums[0:3])
    if closest>target:
        return closest
    closest=sum(nums[-3:])
    if closest<target:
        return closest
    for i in range(len(nums)):
        b=i+1
        c=len(nums)-1
        while b<c:
            sums=nums[i]+nums[b]+nums[c]
            if abs(target-sums)<abs(target-closest):
                closest = sums
            elif sums<target:
                b+=1               
            else:
                c-=1
                
    return closest

if __name__ == '__main__':
    n1, t1 = [-1, 2, 1 -4], 1
    n2, t2 = [0, 0, 0], 1

    print(threeSumClosest(n1, t1))
    print(threeSumClosest(n2, t2))
