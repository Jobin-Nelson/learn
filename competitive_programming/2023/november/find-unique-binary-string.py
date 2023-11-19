'''
Created Date: 2023-11-16
Qn: Given an array of strings nums containing n unique binary strings each of
    length n, return a binary string of length n that does not appear in nums.
    If there are multiple answers, you may return any of them.
Link: https://leetcode.com/problems/find-unique-binary-string/
Notes:
    - iterate over each nums and each string simultaneously and flip the bit
'''
def findDifferentBinaryString(nums: list[str]) -> str:
    return ''.join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))

if __name__ == '__main__':
    n1 = ["01", "10"]
    n2 = ["00", "01"]
    n3 = ["111", "011", "001"]

    print(findDifferentBinaryString(n1))
    print(findDifferentBinaryString(n2))
    print(findDifferentBinaryString(n3))
