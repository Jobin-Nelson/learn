"""
Created Date: 2024-06-10
Qn: A school is trying to take an annual photo of all the students. The
    students are asked to stand in a single file line in non-decreasing order
    by height. Let this ordering be represented by the integer array expected
    where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that
    the students are standing in. Each heights[i] is the height of the ith
    student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].
Link: https://leetcode.com/problems/height-checker/
Notes:
    - use sorting
"""
def heightChecker(heights: list[int]) -> int:
    expected = sorted(heights)
    res = 0
    for h, e in zip(heights, expected):
        if h != e: res += 1
    return res

if __name__ == '__main__':
    h1 = [1, 1, 4, 2, 1, 3]
    h2 = [5,1, 2, 3, 4]
    h3 = list(range(1, 6))

    print(heightChecker(h1))
    print(heightChecker(h2))
    print(heightChecker(h3))
