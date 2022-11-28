'''
Qn: Design a HashSet without using any built-in hash table libraries.
Link: https://leetcode.com/problems/design-hashset/
Notes:
    - use list to store keys, use nested loops to save space
'''
class MyHashSet:
    def __init__(self):
        self.array = [[] for _ in range(1000)]
    def add(self, key: int) -> None:
        subkey = key % 1000
        if not self.contains(key):
            self.array[subkey].append(key)
    def remove(self, key: int) -> None:
        subkey = key % 1000
        if self.contains(key):
            self.array[subkey].remove(key)
    def  contains(self, key: int) -> bool:
        subkey = key % 1000
        return key in self.array[subkey]

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))
