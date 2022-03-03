'''
Qn: Given the two integers m and n,
return the number of possible unique paths that the robot can take to reach the bottom-right corner.
Link: https://leetcode.com/problems/unique-paths/
Notes: 
- creating a 2d array with m, n 
- adding up the values from boht bottom and right side to get the total possible ways to reach the end of matrix from the beginning
'''
def unique_path(m, n):
    row = [1] * n

    for i in range(m-1):
        new_row = [1]*n
        for j in range(n-2, -1, -1):
            new_row[j] = new_row[j+1] + row[j]
        row = new_row
    return row[0]

if __name__ == '__main__':
    m1, n1 = 3, 7
    m2, n2 = 3, 2
    print(unique_path(m1, n1))
    print(unique_path(m2, n2))