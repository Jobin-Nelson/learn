"""
Created Date: 2024-07-09
Qn: There is a restaurant with a single chef. You are given an array customers,
    where customers[i] = [arrivali, timei]:

    - arrivali is the arrival time of the ith customer. The arrival times are
      sorted in non-decreasing order. 
    - timei is the time needed to prepare the order of the ith customer. 

    When a customer arrives, he gives the chef his
    order, and the chef starts preparing it once he is idle. The customer waits
    till the chef finishes preparing his order. The chef does not prepare food
    for more than one customer at a time. The chef prepares food for customers
    in the order they were given in the input.

    Return the average waiting time of all customers. Solutions within 10-5
    from the actual answer are considered accepted.
Link: https://leetcode.com/problems/average-waiting-time/
Notes:
    - use simulation
"""
def averageWaitingTime(customers: list[list[int]]) -> float:
    prev_time = 0
    res = 0
    for a, w in customers:
        cur_time = max(a, prev_time) + w
        res += cur_time - a
        prev_time = cur_time
    return res / len(customers)


if __name__ == '__main__':
    c1 = [[1,2],[2,5],[4,3]]
    c2 = [[5,2],[5,4],[10,3],[20,1]]

    print(averageWaitingTime(c1))
    print(averageWaitingTime(c2))
