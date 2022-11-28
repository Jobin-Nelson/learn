'''
Created Date: 2022-11-11
Qn: Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages,
    you must instead have the result be placed in the first part of the array
    nums. More formally, if there are k elements after removing the duplicates,
    then the first k elements of nums should hold the final result. It does not
    matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by
    modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    ```java
    int[] nums = [...]; // Input array 
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length; 
    for (int i = 0; i < k; i++) { 
        assert nums[i] == expectedNums[i];
    }
    ```
    If all assertions pass, then your solution will be accepted.
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Notes:
    - have a counter from 1, this can act as an index as well
    - we just want to make sure that the value at each index is different
'''
def removeDuplicates(nums: list[int]) -> int:
    if not nums: return 0
    res = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[res] = nums[i+1]
            res += 1
    return res

if __name__ == '__main__':
    n1 = [1,1,2]
    n2 = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(n1))
    print(removeDuplicates(n2))
