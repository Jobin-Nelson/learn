"""
Created Date: 2024-05-26
Qn: An attendance record for a student can be represented as a string where
    each character signifies whether the student was absent, late, or present
    on that day. The record only contains the following three characters:

        - 'A': Absent. 
        - 'L': Late. 
        - 'P': Present.

    Any student is eligible for an attendance award if they meet both of the
    following criteria:

        - The student was absent ('A') for strictly fewer than 2 days total. 
        - The student was never late ('L') for 3 or more consecutive days.

    Given an integer n, return the number of possible attendance records of
    length n that make a student eligible for an attendance award. The answer
    may be very large, so return it modulo 109 + 7.
Link: https://leetcode.com/problems/student-attendance-record-ii/
Notes:
    - use iterative dp
"""
def checkRecord(n: int) -> int:
    MOD = 10 ** 9 + 7
    dp_next_state = [[0] * 3 for _ in range(2)]
    dp_cur_state = [[0] * 3 for _ in range(2)]

    dp_cur_state[0][0] = 1

    for _ in range(n):
        for total_absences in range(2):
            for consecutive_lates in range(3):
                # if picking 'P'
                dp_next_state[total_absences][0] = (
                    dp_next_state[total_absences][0] + dp_cur_state[total_absences][consecutive_lates]
                ) % MOD

                # if picking 'A'
                if total_absences < 1:
                    dp_next_state[total_absences+1][0] = (
                        dp_next_state[total_absences+1][0] + dp_cur_state[total_absences][consecutive_lates]
                    ) % MOD

                # if picking 'L'
                if consecutive_lates < 2:
                    dp_next_state[total_absences][consecutive_lates+1] = (
                        dp_next_state[total_absences][consecutive_lates+1] + dp_cur_state[total_absences][consecutive_lates]
                    ) % MOD

        dp_cur_state = [row[:] for row in dp_next_state]
        dp_next_state = [[0] * 3 for _ in range(2)]

    return sum(val for rows in dp_cur_state for val in rows) % MOD

if __name__ == '__main__':
    n1 = 2
    n2 = 1
    n3 = 10101

    print(checkRecord(n1))
    print(checkRecord(n2))
    print(checkRecord(n3))
