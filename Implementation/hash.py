# for single no. in one hash value.

class HashTable:
    def __init__(self) -> None:
        self.max = 100
        self.arr = [None] * self.max
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['march 6'] = 120
t['dec 6'] = 189
t['feb 18'] = 166
t['march 17'] = 170


t['march 6']