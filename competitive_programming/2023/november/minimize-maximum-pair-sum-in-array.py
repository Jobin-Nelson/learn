'''
Created Date: 2023-11-17
Qn: The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the
    largest pair sum in a list of pairs.

        - For example, if we have pairs (1,5), (2,3), and (4,4), the maximum
          pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

    Given an array nums of even length n, pair up the elements of nums into n /
    2 pairs such that:

        - Each element of nums is in exactly one pair, and 
        - The maximum pair sum is minimized.

    Return the minimized maximum pair sum after optimally pairing up the
    elements.
Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
Notes:
    - sort and pair the first element with the last one
'''
def minPairSum(nums :list[int]) -> int:
    nums.sort()
    N = len(nums)
    return max(nums[i] + nums[N-i-1] for i in range(N//2))

if __name__ == '__main__':
    n1 = [3, 5, 2, 3]
    n2 = [3, 5, 4, 2, 4, 6]

    print(minPairSum(n1))
    print(minPairSum(n2))
