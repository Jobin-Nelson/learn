"""
Created Date: 2024-04-08
Qn: The school cafeteria offers circular and square sandwiches at lunch break,
    referred to by numbers 0 and 1 respectively. All students stand in a queue.
    Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of
    students. The sandwiches are placed in a stack. At each step:

        - If the student at the front of the queue prefers the sandwich on the
          top of the stack, they will take it and leave the queue. 
        - Otherwise, they will leave it and go to the queue's end.

    This continues until none of the queue students want to take the top
    sandwich and are thus unable to eat.

    You are given two integer arrays students and sandwiches where
    sandwiches[i] is the type of the i^th
    sandwich in the stack (i = 0 is the top of the stack) and students[j] is
    the preference of the j^th student in
    the initial queue (j = 0 is the front of the queue). Return the number of
    students that are unable to eat.
Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
Notes:
    - use deque to simulate the above condition
    - use counter
"""
from collections import deque, Counter

def countStudents(students: list[int], sandwiches: list[int]) -> int:
    count = Counter(students)
    for sandwich in sandwiches:
        if count[sandwich] == 0: break
        count[sandwich] -= 1
    return count.total()
    # q = deque(students)
    #
    # for sandwich in sandwiches:
    #     for _ in range(len(q)):
    #         student = q.popleft()
    #         if student == sandwich: break
    #         q.append(student)
    #     else:
    #         break
    # return len(q)

if __name__ == '__main__':
    students1, sandwiches1 =[1,1,0,0], [0, 1, 0, 1]
    students2, sandwiches2 =[1,1,1,0,0,1], [1, 0, 0, 0, 1,1]

    print(countStudents(students1, sandwiches1))
    print(countStudents(students2, sandwiches2))
