'''
Created Date: 2022-11-30
Qn: Given an array of integers arr, return true if the number of occurrences of
    each value in the array is unique, or false otherwise.
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Notes:
    - use hashmap to count values and set to see if they are unique
'''
def uniqueOccurences(arr: list[int]) -> bool:
    lookup = dict()

    for n in arr:
        lookup[n] = lookup.get(n, 0) + 1
    if len(set(lookup.values())) != len(set(arr)): return False
    return True

if __name__ == '__main__':
    a1 = [1,2,2,1,1,3]
    a2 = [1, 2]
    a3 = [-3,0,1,-3,1,1,1,-3,10,0]

    print(uniqueOccurences(a1))
    print(uniqueOccurences(a2))
    print(uniqueOccurences(a3))
