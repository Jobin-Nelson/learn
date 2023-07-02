'''
Created Date: 2023-06-30
Qn: There is a 1-based binary matrix where 0 represents land and 1 represents
    water. You are given integers row and col representing the number of rows
    and columns in the matrix, respectively.

    Initially on day 0, the entire matrix is land. However, each day a new cell
    becomes flooded with water. You are given a 1-based 2D array cells, where
    cells[i] = [ri, ci] represents that on the ith day, the cell on the rith
    row and cith column (1-based coordinates) will be covered with water (i.e.,
    changed to 1).

    You want to find the last day that it is possible to walk from the top to
    the bottom by only walking on land cells. You can start from any cell in
    the top row and end at any cell in the bottom row. You can only travel in
    the four cardinal directions (left, right, up, and down).

    Return the last day where it is possible to walk from the top to the bottom
    by only walking on land cells.
Link: https://leetcode.com/problems/last-day-where-you-can-still-cross/
Notes:
    - possible solutions
        - binary search + BFS
        - binary search + DFS
        - Union Find on land
        - Union Find on water
'''
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        res = x
        while self.parent[res] != res:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, n1: int, n2: int):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return 
        if self.rank[p1] > self.rank[p2]: p1, p2 = p2, p1
        self.parent[p1] = p2
        self.rank[p2] += self.rank[p1]

def latestDayToCross(row: int, col: int, cells: list[list[int]]) -> int:
    uf = UnionFind(row * col + 2)
    grid = [[0] * col for _ in range(row)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(row * col):
        r, c = cells[i][0] - 1, cells[i][1] - 1
        grid[r][c] = 1
        index_1 = r * col + c + 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                index_2 = nr * col + nc + 1
                uf.union(index_1, index_2)
            if c == 0: uf.union(0, index_1)
            if c == col - 1: uf.union(row * col + 1, index_1)
            if uf.find(0) == uf.find(row * col + 1): return i

if __name__ == '__main__':
    ro1, co1, ce1 = 2, 2, [[1,1],[2,1],[1,2],[2,2]]
    ro2, co2, ce2 = 2, 2, [[1,1],[1,2],[2,1],[2,2]]
    ro3, co3, ce3 = 3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

    print(latestDayToCross(ro1, co1, ce1))
    print(latestDayToCross(ro2, co2, ce2))
    print(latestDayToCross(ro3, co3, ce3))
    
