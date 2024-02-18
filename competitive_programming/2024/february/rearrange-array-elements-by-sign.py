"""
Created Date: 2024-02-14
Qn: You are given a 0-indexed integer array nums of even length consisting of
    an equal number of positive and negative integers.

    You should rearrange the elements of nums such that the modified array
    follows the given conditions:

        - Every consecutive pair of integers have opposite signs. 
        - For all integers with the same sign, the order in which they were
          present in nums is preserved. 
        - The rearranged array begins with a positive integer.

    Return the modified array after rearranging the elements to satisfy the
    aforementioned conditions.
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Notes:
    - use two pointers or two stacks
"""
def rearrangeArray(nums: list[int]) -> list[int]:
    pos, neg = [], []

    for n in nums:
        if n > 0:
            pos.append(n)
        else:
            neg.append(n)
    res = []
    for pn, nn in zip(pos, neg):
        res.append(pn)
        res.append(nn)
    return res

if __name__ == '__main__':
    n1 = [3,1,-2,-5,2,-4]
    n2 = [-1, 1]

    print(rearrangeArray(n1))
    print(rearrangeArray(n2))
