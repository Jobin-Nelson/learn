class hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] # initializing the hashtable with length = max

    def get_hash(self, key): # function to get the index from the key
        h = 0
        for ch in key:
            h += ord(ch)

        return h % self.MAX

    def __setitem__(self, key, value):
        ind = self.get_hash(key)
        for id, n in enumerate(self.arr[ind]):
            if len(n) == 2 and n[0] == key:
                self.arr[ind][id] = (key, value)
                return
        else:
            self.arr[ind].append((key, value))

    def __getitem__(self, key):
        ind = self.get_hash(key)
        for el in  self.arr[ind]:
            if el[0] == key:
                return el[1]

    def __delitem__(self, key):
        ind = self.get_hash(key)
        for id, el in enumerate(self.arr[ind]):
            if el[0] == key:
                del self.arr[ind][id]
                break


if __name__ == '__main__':
    t = hash_table()
    t['Jobin'] = '7356507788'
    t['Jaison'] = '94567369349'
    print('Phone number of Jobin: ', t['Jobin'])
    print('Phone number of Jaison: ', t['Jaison'])
    t['march 6'] = 10
    t['march 17'] = 21
    print( t['march 6'])
    print(t['march 17'])
    del t['march 17']
    print(t['march 17'])
