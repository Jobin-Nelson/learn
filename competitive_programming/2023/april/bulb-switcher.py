'''
Created Date: 2023-04-27
Qn: There are n bulbs that are initially off. You first turn on all the bulbs,
    then you turn off every second bulb.

    On the third round, you toggle every third bulb (turning on if it's off or
    turning off if it's on). For the ith round, you toggle every i bulb. For
    the nth round, you only toggle the last bulb.

    Return the number of bulbs that are on after n rounds.
Link: https://leetcode.com/problems/bulb-switcher/
Notes:
    - a bulb will only be on after n rounds if it was toggled an odd number
      of times
    - and for the bulb to be toggled an odd number of times, if the bulb is in
      perfect square position
    - so to find the number of bulbs that stay on, we need to find the number
      of perfect squares within 1-n
    - this can be calculated by √n rounded to integer
'''
import math

def bulbSwitch(n: int) -> int:
    return int(math.sqrt(n))

if __name__ == '__main__':
    n1 = 3
    n2 = 0
    n3 = 1

    print(bulbSwitch(n1))
    print(bulbSwitch(n2))
    print(bulbSwitch(n3))
