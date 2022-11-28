'''
Qn: Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
    such that i < j < k and nums[i] < nums[k] < nums[j].
    Return true if there is a 132 pattern in nums, otherwise, return false.
Link: https://leetcode.com/problems/132-pattern/
Notes:
'''
def find132pattern(nums: list[int]) -> bool:
    N = len(nums)
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False
                

if __name__ == '__main__':
    n1 = [1, 2, 3, 4]
    n2 = [3, 1, 4, 2]
    n3 = [-1, 3, 2, 0]
    print(find132pattern(n1))
    print(find132pattern(n2))
    print(find132pattern(n3))
