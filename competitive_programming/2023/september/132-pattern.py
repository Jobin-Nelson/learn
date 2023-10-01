'''
Created Date: 2023-09-30
Qn: Given an array of n integers nums, a 132 pattern is a subsequence of three
    integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] <
    nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.
Link: https://leetcode.com/problems/132-pattern/
Notes:
    - use monotonic decreasing stack
'''
def find132pattern(nums: list[int]) -> bool:
    stack = []
    cur_min = nums[0]

    for n in nums[1:]:
        while stack and n >= stack[-1][0]: stack.pop()
        if stack and n < stack[-1][0] and n > stack[-1][1]: return True
        stack.append([n, cur_min])
        cur_min = min(cur_min, n)
    return False

if __name__ == '__main__':
    n1 = [1,2,3,4]
    n2 = [3,1,4,2]
    n3 = [-1,3,2,0]

    print(find132pattern(n1))
    print(find132pattern(n2))
    print(find132pattern(n3))
