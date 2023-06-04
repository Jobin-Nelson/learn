'''
Created Date: 2023-05-31
Qn: An underground railway system is keeping track of customer travel times
    between different stations. They are using this data to calculate the
    average time it takes to travel from one station to another.

    Implement the UndergroundSystem class:

        - void checkIn(int id, string stationName, int t)
            - A customer with a card ID equal to id, checks in at the station
              stationName at time t. 
            - A customer can only be checked into one place at a time.
        - void checkOut(int id, string stationName, int t)
            - A customer with a card ID equal to id, checks out from the
              station stationName at time t.
        - double getAverageTime(string startStation, string endStation)
            - Returns the average time it takes to travel from startStation to
              endStation.
            - The average time is computed from all the previous traveling
              times from startStation to endStation that happened directly,
              meaning a check in at startStation followed by a check out from
              endStation.
            - The time it takes to travel from startStation to endStation may
              be different from the time it takes to travel from endStation to
              startStation.
            - There will be at least one customer that has traveled from
              startStation to endStation before getAverageTime is called.

    You may assume all calls to the checkIn and checkOut methods are
    consistent. If a customer checks in at time t1 then checks out at time t2,
    then t1 < t2. All events happen in chronological order.
Link: https://leetcode.com/problems/design-underground-system/
Notes:
    - use 2 hashmaps
'''
class UndergroundSystem:
    def __init__(self):
        self.stage = {}
        self.graph = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stage[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.stage.pop(id)
        route = (startStation, stationName)
        if route not in self.graph: self.graph[route] = [0, 0]
        self.graph[route][0] += t - startTime
        self.graph[route][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.graph[(startStation, endStation)]
        return total / count

if __name__ == '__main__':
    u = UndergroundSystem()
    u.checkIn(45, 'Leyton', 3)
    u.checkIn(32, 'Paradise', 8)
    u.checkIn(27, 'Leyton', 10)
    u.checkOut(45, 'WaterLoo', 15)
    u.checkOut(27, 'WaterLoo', 20)
    u.checkOut(32, 'Cambridge', 22)
    print(u.getAverageTime('Paradise', 'Cambridge'))
    print(u.getAverageTime('Leyton', 'WaterLoo'))
    u.checkIn(10, 'Leyton', 24)
    print(u.getAverageTime('Leyton', 'WaterLoo'))
    u.checkOut(10, 'WaterLoo', 38)
    print(u.getAverageTime('Leyton', 'WaterLoo'))
