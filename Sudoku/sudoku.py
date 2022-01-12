import numpy as np

def possible(y,x,n):
    global grid
    #check row 
    for i in range(9):
        if grid[y][i]==n:
            return False
    #check column 
    for i in range(9):
        if grid[i][x]==n:
            return False
    #check box
    box_x = (x//3)*3
    box_y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[box_y+i][box_x+j]==n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return 
    print(np.matrix(grid))
    input("More?")

if __name__=='__main__':
    grid =[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]
    solve()
