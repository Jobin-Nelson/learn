def maxArea(heights: list[int]) -> int:
    N = len(heights)
    l, r = 0, N - 1
    res = 0
    while l < r:
        hl, hr = heights[l], heights[r]
        height = min(hl, hr)
        width = r - l
        cur_area = width * height
        res = max(res, cur_area)
        if hl < hr:
            l += 1
        else:
            r -= 1

    return res


if __name__ == "__main__":
    h1 = [1, 7, 2, 5, 4, 7, 3, 6]
    h2 = [2] * 3

    print(maxArea(h1))
    print(maxArea(h2))
