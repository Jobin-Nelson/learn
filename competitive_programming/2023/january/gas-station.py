'''
Created Date: 2023-01-07
Qn: There are n gas stations along a circular route, where the amount of gas at
    the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to
    travel from the ith station to its next (i + 1)th station. You begin the
    journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's
    index if you can travel around the circuit once in the clockwise direction,
    otherwise return -1. If there exists a solution, it is guaranteed to be
    unique
Link: https://leetcode.com/problems/gas-station/
Notes:
    Here's the plan:

        - First, it is possible to complete the circuit if and only if the
          total amount of gas on the circuit is sufficient to drive the
          circuit. More formally: sum(gas) >= sum(cost).
        - The starting station can be determined by starting at some
          stationa(say, a = 0) and noting whether a station b on the circuit is
          unreachable due to lack of gas. If all are reachable, then a is our
          answer. If not, the start is not anor is any station between a andb.
        - We reset the tank to zero and repeat.
        - The last station that is unreachable in this process, say stationz,
          is our answer.

    Why does this work? Recall there's enough gas to complete the circuit. If
    it were possible to "borrow" gas to get to the next station, the station
    requiring the most borrowed gas overall is station 'z'. Thus, starting at
    station 'z' is the answer.
'''
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost): return -1

    tank = idx = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0: tank, idx = 0, i + 1
    return idx

if __name__ == '__main__':
    g1, c1 = [1,2,3,4,5], [3,4,5,1,2]
    g2, c2 = [2,3,4], [3,4,3]

    print(canCompleteCircuit(g1, c1))
    print(canCompleteCircuit(g2, c2))
