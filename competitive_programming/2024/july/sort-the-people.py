"""
Created Date: 2024-07-22
Qn: You are given an array of strings names, and an array heights that consists
    of distinct positive integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the
    ith person.

    Return names sorted in descending order by the people's heights.
Link: https://leetcode.com/problems/sort-the-people/
Notes:
    - use pythons sort or implement merge sort
"""
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    si = sorted(range(len(names)), key=lambda x: heights[x], reverse=True)
    return [names[i] for i in si]

if __name__ == '__main__':
    n1, h1 = ["Mary","John","Emma"], [180,165,170]
    n2, h2 = ["Alice","Bob","Bob"], [155,185,150]

    print(sortPeople(n1, h1))
    print(sortPeople(n2, h2))
