'''
Created Date: 2022-11-25
Qn: Given an array of integers arr, find the sum of min(b), where b ranges over
    every (contiguous) subarray of arr. Since the answer may be large, return
    the answer modulo 10⁹ + 7.
Link: https://leetcode.com/problems/sum-of-subarray-minimums/
Notes:
    - build monotonously non-decreasing stack and then find previous less or
      equal value and reuse it's sum
'''
def sumSubArrayMins(arr: list[int]) -> int:
    arr = [0] + arr
    stack = [0]
    res = [0] * len(arr)

    for i in range(len(arr)):
        while arr[stack[-1]] > arr[i]:
            stack.pop()
        j = stack[-1]
        res[i] = res[j] + (i-j) * arr[i]
        stack.append(i)
    return sum(res) % (10**9+7)

if __name__ == '__main__':
    a1 = [3, 1, 2, 4]
    a2 = [11, 81, 94, 43, 3]
    
    print(sumSubArrayMins(a1))
    print(sumSubArrayMins(a2))
