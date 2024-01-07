"""
Created Date: 2024-01-01
Qn: Assume you are an awesome parent and want to give your children some
    cookies. But, you should give each child at most one cookie.

    Each child i has a greed factor g[i], which is the minimum size of a cookie
    that the child will be content with; and each cookie j has a size s[j]. If
    s[j] >= g[i], we can assign the cookie j to the child i, and the child i
    will be content. Your goal is to maximize the number of your content
    children and output the maximum number.
Link: https://leetcode.com/problems/assign-cookies/
Notes:
    - sort both arrays and iterate until content value is smaller than size value
"""
def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    res = 0
    for c in s:
        if res >= len(g): return res
        if c >= g[res]: res += 1
    return res

if __name__ == '__main__':
    g1, s1 = [1, 2, 3], [1, 1]
    g2, s2 = [1, 2], [1, 2, 3]
    g3, s3 = [10,9,8,7], [5,6,7,8]

    print(findContentChildren(g1, s1))
    print(findContentChildren(g2, s2))
    print(findContentChildren(g3, s3))
