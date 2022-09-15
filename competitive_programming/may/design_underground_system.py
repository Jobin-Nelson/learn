'''
Qn: An underground railway system is keeping track of customer travel times between different stations. 
They are using this data to calculate the average time it takes to travel from one station to another.
Link: https://leetcode.com/problems/design-underground-system/
Notes:
    - use two hashmaps
    - think only about the output
'''
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.i = defaultdict(tuple)
        self.o = defaultdict(list)

    def checkIn(self, id: int, stationName:str, t: int) -> None:
        self.i[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.i[id]
        total = t - startTime
        self.o[(startStation, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(startStation, endStation)]) / len(self.o[(startStation, endStation)])

if __name__ == '__main__':
    print('For object 1')
    obj1 = UndergroundSystem()
    obj1.checkIn(45, 'Leyton', 3)
    obj1.checkIn(45, "Leyton", 3)
    obj1.checkIn(32, "Paradise", 8)
    obj1.checkIn(27, "Leyton", 10)
    obj1.checkOut(45, "Waterloo", 15)
    obj1.checkOut(27, "Waterloo", 20)
    obj1.checkOut(32, "Cambridge", 22)
    print(obj1.getAverageTime("Paradise", "Cambridge"))
    print(obj1.getAverageTime("Leyton", "Waterloo"))
    obj1.checkIn(10, "Leyton", 24)
    print(obj1.getAverageTime("Leyton", "Waterloo"))
    obj1.checkOut(10, "Waterloo", 38)
    print(obj1.getAverageTime("Leyton", "Waterloo"))

    print('\nFor object 2')
    obj2 = UndergroundSystem()
    obj2.checkIn(10, "Leyton", 3)
    obj2.checkOut(10, "Paradise", 8)
    print(obj2.getAverageTime("Leyton", "Paradise"))
    obj2.checkIn(5, "Leyton", 10)
    obj2.checkOut(5, "Paradise", 16)
    print(obj2.getAverageTime("Leyton", "Paradise"))
    obj2.checkIn(2, "Leyton", 21)
    obj2.checkOut(2, "Paradise", 30)
    print(obj2.getAverageTime("Leyton", "Paradise"))
