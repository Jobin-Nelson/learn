'''
Qn: There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a
Link: https://leetcode.com/problems/course-schedule/
Notes: 
- build adjacency list
- depth first traversal and remove course and return True for each course
'''

def can_finish(num_courses, prerequisites):
    pre_map = {i: [] for i in range(num_courses)}

    for crs, pre in prerequisites:
        pre_map[crs].append(pre)
    
    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        if pre_map[crs] == []:
            return True
        visited.add(crs)
        for neighbor in pre_map[crs]:
            if not dfs(neighbor):
                return False
        visited.remove(crs)
        pre_map[crs] = []
        return True

    for crs in range(num_courses):
        if not dfs(crs):
            return False
    return True
                

if __name__ == '__main__':
    prerequisites1, prerequisites2 = [[1,0]], [[1, 0], [0, 1]]
    num_courses1, num_courses2 = 2, 2
    print(can_finish(num_courses1, prerequisites1))
    print(can_finish(num_courses2, prerequisites2))