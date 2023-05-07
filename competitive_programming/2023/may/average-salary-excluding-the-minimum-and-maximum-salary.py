'''
Created Date: 2023-05-01
Qn: You are given an array of unique integers salary where salary[i] is the
    salary of the ith employee.

    Return the average salary of employees excluding the minimum and maximum
    salary. Answers within 10-5 of the actual answer will be accepted.
Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
Notes:
    - find average of n-2 deduct max and min
'''
def average(salary: list[int]) -> float:
    min_salary = min(salary)
    max_salary = max(salary)
    total_salary = sum(salary) - min_salary - max_salary
    return total_salary / (len(salary) - 2)

if __name__ == '__main__':
    s1 = [4000,3000,1000,2000]
    s2 = [1000,2000,3000]

    print(average(s1))
    print(average(s2))
