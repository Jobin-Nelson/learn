'''
Qn: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Notes: 
'''
def longest_consecutive(nums):
    longest = 0
    num_set = set(nums)

    for n in nums:
        if (n-1) not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest

if __name__ == '__main__':
    n1, n2 = [100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]
    print(longest_consecutive(n1))
    print(longest_consecutive(n2))