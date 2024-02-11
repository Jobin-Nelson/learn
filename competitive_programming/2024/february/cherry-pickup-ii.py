"""
Created Date: 2024-02-11
Qn: You are given a rows x cols matrix grid representing a field of cherries
    where grid[i][j] represents the number of cherries that you can collect
    from the (i, j) cell.

    You have two robots that can collect cherries for you:

        - Robot #1 is located at the top-left corner (0, 0), and 
        - Robot #2 is located at the top-right corner (0, cols - 1).

    Return the maximum number of cherries collection using both robots by
    following the rules below:

        - From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1,
          j), or (i + 1, j + 1). 
        - When any robot passes through a cell, It picks up all cherries, and
          the cell becomes an empty cell. 
        - When both robots stay in the same cell, only one takes the cherries. 
        - Both robots cannot move outside of the grid at any moment. 
        - Both robots should reach the bottom row in grid.

Link: https://leetcode.com/problems/cherry-pickup-ii/
Notes:
"""
def cherryPickup(grid: list[list[int]]) -> int:
    pass

if __name__ == '__main__':
    g1 = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    g2 = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

    print(cherryPickup(g1))
    print(cherryPickup(g2))
