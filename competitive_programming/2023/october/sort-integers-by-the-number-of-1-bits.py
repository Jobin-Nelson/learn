'''
Created Date: 2023-10-30
Qn: You are given an integer array arr. Sort the integers in the array in
    ascending order by the number of 1's in their binary representation and in
    case of two or more integers have the same number of 1's you have to sort
    them in ascending order.

    Return the array after sorting it.
Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
Notes:
    - use bit_count and num itself
'''
def sortByBits(arr: list[int]) -> list[int]:
    # return sorted(arr, key=lambda x: (x.bit_count(), x))  
    def find_weight(num: int) -> int:
        weight = 0
        while num:
            weight += 1
            num &= (num-1)
        return weight
    return sorted(arr, key=lambda x: (find_weight(x), x))

if __name__ == '__main__':
    a1 = list(range(9))
    a2 = [1024,512,256,128,64,32,16,8,4,2,1]

    print(sortByBits(a1))
    print(sortByBits(a2))
