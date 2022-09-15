'''
Created Date: 23-06-2022
Qn: There are n different online courses numbered from 1 to n. 
    You are given an array courses where courses[i] = [durationi, lastDayi] 
    indicate that the ith course should be taken continuously for duration i 
    days and must be finished before or on lastDayi.
    You will start on the 1st day and you cannot take two or more courses 
    simultaneously.
    Return the maximum number of courses that you can take.
Link: https://leetcode.com/problems/course-schedule-iii/
Notes:
    - use heap to track the biggest duration and pop when max time exceeds end time
    - return the length of heap
'''
import heapq

def scheduleCourse(courses: list[list[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    max_time = 0

    heap = []
    for time, end_time in courses:
        heapq.heappush(heap, -time)
        max_time += time

        if max_time > end_time:
            big_time = heapq.heappop(heap)
            max_time += big_time
    return len(heap)

if __name__ == '__main__':
    c1 = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    c2 = [[1,2]]
    c3 = [[3,2],[4,3]]
    print(scheduleCourse(c1))
    print(scheduleCourse(c2))
    print(scheduleCourse(c3))
