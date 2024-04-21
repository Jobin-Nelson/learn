"""
Created Date: 2024-04-20
Qn: You are given a 0-indexed m x n binary matrix land where a 0 represents a
    hectare of forested land and a 1 represents a hectare of farmland.

    To keep the land organized, there are designated rectangular areas of
    hectares that consist entirely of farmland. These rectangular areas are
    called groups. No two groups are adjacent, meaning farmland in one group is
    not four-directionally adjacent to another farmland in a different group.

    land can be represented by a coordinate system where the top left corner of
    land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the
    coordinates of the top left and bottom right corner of each group of
    farmland. A group of farmland with a top left corner at (r1, c1) and a
    bottom right corner at (r2, c2) is represented by the 4-length array [r1,
    c1, r2, c2].

    Return a 2D array containing the 4-length arrays described above for each
    group of farmland in land. If there are no groups of farmland, return an
    empty array. You may return the answer in any order.
Link: https://leetcode.com/problems/find-all-groups-of-farmland/
Notes:
    - use grid itself to mark visited
"""
def findFarmland(land: list[list[int]]) -> list[list[int]]:
    R, C = len(land), len(land[0])
    dirs = [1, 0, -1, 0, 1]

    def dfs(r: int, c: int) -> list[int]:
        if 0 <= r < R and 0 <= c < C and land[r][c] == 1:
            land[r][c] = 0
            res = [r, c]
            for i in range(len(dirs)-1):
                dx, dy = r + dirs[i], c + dirs[i+1]
                nei_res = dfs(dx, dy)
                if not nei_res: continue
                res[0] = max(res[0], nei_res[0])
                res[1] = max(res[1], nei_res[1])
            return res
        return []

    res = []
    for r in range(R):
        for c in range(C):
            if land[r][c] == 1:
                er, ec = dfs(r, c)
                res.append([r, c, er, ec])
    return res



if __name__ == '__main__':
    l1 = [[1,0,0],[0,1,1],[0,1,1]]
    l2 = [[1,1],[1,1]] 
    l3 = [[0]]

    print(findFarmland(l1))
    print(findFarmland(l2))
