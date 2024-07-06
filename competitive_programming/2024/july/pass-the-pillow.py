"""
Created Date: 2024-07-06
Qn: There are n people standing in a line labeled from 1 to n. The first person
    in the line is holding a pillow initially. Every second, the person holding
    the pillow passes it to the next person standing in the line. Once the
    pillow reaches the end of the line, the direction changes, and people
    continue passing the pillow in the opposite direction.

        - For example, once the pillow reaches the nth person they pass it to
          the n - 1th person, then to the n - 2th person and so on.

    Given the two positive integers n and time, return the index of the person
    holding the pillow after time seconds.
Link: https://leetcode.com/problems/pass-the-pillow/
Notes:
    - use math
"""
def passThePillow(n: int, time: int) -> int:
    count, rem = divmod(time, n-1)
    if count & 1:
        return n - rem
    return rem + 1

if __name__ == '__main__':
    n1, t1 = 4, 5
    n2, t2 = 3, 2
    n3, t3 = 9, 4
    n4, t4 = 18, 38

    print(passThePillow(n1, t1))
    print(passThePillow(n2, t2))
    print(passThePillow(n3, t3))
    print(passThePillow(n4, t4))
