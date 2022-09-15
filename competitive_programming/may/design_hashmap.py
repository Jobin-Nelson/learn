'''
Qn: Design a HashMap without using any built-in hash table libraries.
Link: https://leetcode.com/problems/design-hashmap/
Notes: 
    - use list to store 10^6 elements
'''
class HashMap:
    def __init__(self):
        self.array = [-1 for _ in range(10**6+1)]
    def put(self, key: int, value: int) -> None:
        self.array[key] = value
    def get(self, key: int) -> int:
        return self.array[key]
    def remove(self, key: int) -> None:
        self.array[key] = -1

if __name__ == '__main__':
    obj = HashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    print(obj.get(3))
    obj.put(2, 1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))
