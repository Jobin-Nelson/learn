'''
Created Date: 2023-10-29
Qn: There are buckets buckets of liquid, where exactly one of the buckets is
    poisonous. To figure out which one is poisonous, you feed some number of
    (poor) pigs the liquid to see whether they will die or not. Unfortunately,
    you only have minutesToTest minutes to determine which bucket is poisonous.

    You can feed the pigs according to these steps:

        - Choose some live pigs to feed. 
        - For each pig, choose which buckets to feed it.
        - The pig will consume all the chosen buckets simultaneously and will
          take no time. Each pig can feed from any number of buckets, and each
          bucket can be fed from by any number of pigs. 
        - Wait for minutesToDie minutes. You may not feed any other pigs during
          this time.
        - After minutesToDie minutes have passed, any pigs that have been fed
          the poisonous bucket will die, and all others will survive. 
        - Repeat this process until you run out of time.

    Given buckets, minutesToDie, and minutesToTest, return the minimum number
    of pigs needed to figure out which bucket is poisonous within the allotted
    time.
Link: https://leetcode.com/problems/poor-pigs
Notes:
    - use maths
'''
def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

if __name__ == '__main__':
    b1, d1, t1 = 4, 15, 15
    b2, d2, t2 = 4, 15, 30

    print(poorPigs(b1, d1, t1))
    print(poorPigs(b2, d2, t2))
