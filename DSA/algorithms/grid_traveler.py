# recursion
def grid_traveler(m, n):
    if (m==1) and (n==1):
        return 1
    if (m==0) or (n==0):
        return 0
    return grid_traveler(m-1, n) + grid_traveler(m ,n-1)

# memoization
def grid_traveler_mem(m, n, dict={}):
    key = str(m) + ',' + str(n)
    if key in dict.keys():
        return dict[key]
    if (m==1) and (n==1):
        return 1
    if (m==0) or (n==0):
        return 0

    dict[key] = grid_traveler_mem(m-1, n, dict) + grid_traveler_mem(m ,n-1, dict)
    return dict[key]
    

if __name__ == '__main__':
    print(grid_traveler(1,1))
    print(grid_traveler(2,3))
    print(grid_traveler(3,2))
    print(grid_traveler(3,3))

    print(grid_traveler_mem(1,1))
    print(grid_traveler_mem(2,3))
    print(grid_traveler_mem(3,2))
    print(grid_traveler_mem(3,3))
    print(grid_traveler_mem(19,19))
