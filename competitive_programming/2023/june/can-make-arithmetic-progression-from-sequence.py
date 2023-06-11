'''
Created Date: 2023-06-06
Qn: A sequence of numbers is called an arithmetic progression if the difference
    between any two consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged
    to form an arithmetic progression. Otherwise, return false.
Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
Notes:
    - sort and check diff between adjacent numbers
'''
def canMakeArithmeticProgression(arr: list[int]) -> bool:
    N = len(arr)
    if N < 2: return True
    arr.sort()
    diff = arr[1] - arr[0]
    return all(diff == (arr[i] - arr[i-1]) for i in range(1, N))

if __name__ == '__main__':
    a1 = [3,5,1]
    a2 = [1,2,4]

    print(canMakeArithmeticProgression(a1))
    print(canMakeArithmeticProgression(a2))
