def trap(heights: list[int]) -> int:
    res = 0
    l, r = 0, len(heights) - 1
    maxl, maxr = heights[l], heights[r]
    while l < r:
        if maxl < maxr:
            l += 1
            maxl = max(maxl, heights[l])
            res += maxl - heights[l]
        else:
            r -= 1
            maxr = max(maxr, heights[r])
            res += maxr - heights[r]
    return res


if __name__ == "__main__":
    h1 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

    print(trap(h1))
