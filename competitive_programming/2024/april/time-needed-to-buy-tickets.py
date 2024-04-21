"""
Created Date: 2024-04-09
Qn: There are n people in a line queuing to buy tickets, where the 0th person
    is at the front of the line and the (n - 1)th person is at the back of the
    line.

    You are given a 0-indexed integer array tickets of length n where the
    number of tickets that the ith person would like to buy is tickets[i].

    Each person takes exactly 1 second to buy a ticket. A person can only buy 1
    ticket at a time and has to go back to the end of the line (which happens
    instantaneously) in order to buy more tickets. If a person does not have
    any tickets left to buy, the person will leave the line.

    Return the time taken for the person at position k (0-indexed) to finish
    buying tickets.
Link: https://leetcode.com/problems/time-needed-to-buy-tickets/
Notes:
    - use one pass iteration, considering 2 cases
    - people coming before k, min(tickets[k], tickets[i])
    - people coming after k, takes min(tickets[k]-1, tickets[i]) 
"""
def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    target_tickets = tickets[k]
    if target_tickets == 1: return k + 1

    res = 0
    for i, ticket in enumerate(tickets):
        if i <= k:
            res += min(target_tickets, ticket)
        else:
            res += min(target_tickets-1, ticket)
    return res

if __name__ == '__main__':
    t1, k1 = [2,3,2], 2
    t2, k2 = [5,1,1,1], 0
    t3, k3 = [84,49,5,24,70,77,87,8], 3

    print(timeRequiredToBuy(t1, k1))
    print(timeRequiredToBuy(t2, k2))
    print(timeRequiredToBuy(t3, k3))
