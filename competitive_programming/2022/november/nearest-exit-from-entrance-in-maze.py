'''
Created Date: 2022-11-21
Qn: You are given an m x n matrix maze (0-indexed) with empty cells
    (represented as '.') and walls (represented as '+'). You are also given the
    entrance of the maze, where entrance = [entrancerow, entrancecol] denotes
    the row and column of the cell you are initially standing at.

    In one step, you can move one cell up, down, left, or right. You cannot
    step into a cell with a wall, and you cannot step outside the maze. Your
    goal is to find the nearest exit from the entrance. An exit is defined as
    an empty cell that is at the border of the maze. The entrance does not
    count as an exit.

    Return the number of steps in the shortest path from the entrance to the
    nearest exit, or -1 if no such path exists.
Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
Notes:
    - bfs
    - use generator for faster solution
'''
from collections import deque

def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    # R, C = len(maze), len(maze[0])
    # r, c = entrance
    # q = deque([[r, c, 0]])
    # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # maze[r][c] = '+'
    #
    # while q:
    #     r, c, steps = q.popleft()
    #     if (r==0 or c==0 or r==R-1 or c==C-1) and [r, c] != entrance: return steps
    #     maze[r][c] = '+'
    #     for dr, dc in dirs:
    #         nr, nc = r + dr, c + dc
    #         if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == '.':
    #             q.append([nr, nc, steps+1])
    #
    # return -1
    m, n = len(maze), len(maze[0])
    x, y = entrance
    
    # this lambda checks the exit condition 
    is_exit = lambda i, j : i*j==0 or i==m-1 or j==n-1
    
    # this generator yields allowed directions
    def adj(i,j):
        dirs=[1, 0, -1, 0, 1]
        for d in range(4):
            ii, jj = i + dirs[d], j + dirs[d+1]
            if 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != "+":
                yield ii,jj
        
    dq = deque([(x,y,0)])                      # [1] start from the entrance...
    maze[x][y] = '+'                           #     ...and mark it as visited
    while dq:                                  # [2] while there are still places to go...
        i, j, s = dq.popleft()                 #     ...try going there (don't try, do it!)
        for ii,jj in adj(i,j):                 # [3] look around, make a step...
            maze[ii][jj] = "+"                 #     ...and mark it as visited
            if is_exit(ii,jj) : return s+1     # [4] great, it's the exit!
            dq.append((ii,jj,s+1))             # [5] or maybe not, continue searching
            
    return -1

if __name__ == '__main__':
    m1, e1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]
    m2, e2 = [["+","+","+"],[".",".","."],["+","+","+"]], [1,0]
    m3, e3 = [[".","+"]], [0,0]

    print(nearestExit(m1, e1))
    print(nearestExit(m2, e2))
    print(nearestExit(m3, e3))

