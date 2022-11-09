'''
Created Date: 2022-11-01
Qn: You have a 2-D grid of size m x n representing a box, and you have n balls.
    The box is open on the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell
    that can redirect a ball to the right or to the left.

    - A board that redirects the ball to the right spans the top-left corner to
      the bottom-right corner and is represented in the grid as 1. 
    - A board that redirects the ball to the left spans the top-right corner to
      the bottom-left corner and is represented in the grid as -1. 

    We drop one ball at the top of each column of the box. Each ball can get
    stuck in the box or fall out of the bottom. A ball gets stuck if it hits a
    "V" shaped pattern between two boards or if a board redirects the ball into
    either wall of the box.

    Return an array answer of size n where answer[i] is the column that the
    ball falls out of at the bottom after dropping the ball from the ith column
    at the top, or -1 if the ball gets stuck in the box.
Link: https://leetcode.com/problems/where-will-the-ball-fall/
Notes:
    - maintain a 1d list with index as values
    - key condition we have to check for is v where the ball gets stuck
      when grid[r][c+1] == -grid[r][c]
'''
def findBall(grid: list[list[int]]) -> list[int]:
    m, n = len(grid), len(grid[0])
    res = list(range(n))

    for r in range(m):
        for i in range(n):
            c = res[i]
            if c == -1: continue
            c_next = c + grid[r][c]
            if c_next < 0 or c_next >= n or grid[r][c_next] == -grid[r][c]:
                res[i] = -1
                continue
            res[i] += grid[r][c]
    return res

if __name__ == '__main__':
    g1 = [[1,1,1,-1,-1],
          [1,1,1,-1,-1],
          [-1,-1,-1,1,1],
          [1,1,1,1,-1],
          [-1,-1,-1,-1,-1]]
    g2 = [[-1]]
    g3 = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

    print(findBall(g1))
    print(findBall(g2))
    print(findBall(g3))
