'''
Created Date: 2023-02-15
Qn: The array-form of an integer num is an array representing its digits in
    left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

    Given num, the array-form of an integer, and an integer k, return the
    array-form of the integer num + k.
Link: https://leetcode.com/problems/add-to-array-form-of-integer/
Notes:
    - school addition
    - divmod to carry over
'''
def addToArrayForm(num: list[int], k: int) -> list[int]:
    num[-1] += k
    carry = 0
    for i in range(len(num)-1, -1, -1):
        carry, num[i] = divmod(num[i], 10)
        if i: num[i-1] += carry
    if carry: num = list(map(int, str(carry))) + num
    return num

if __name__ == '__main__':
    n1, k1 = [1, 2, 0, 0], 34
    n2, k2 = [2, 7, 4], 181
    n3, k3 = [2, 1, 5], 806

    print(addToArrayForm(n1, k1))
    print(addToArrayForm(n2, k2))
    print(addToArrayForm(n3, k3))
