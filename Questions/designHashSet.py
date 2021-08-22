# Leetcode: 705. Design hash Set

class MyHashSet:

    def __init__(self):
        self.size =  10000
        self.table = [None] * self.size
    
    def calculate_hashValue(self, key):
        return key % self.size
    
    def add(self, key):
        hv = self.calculate_hashValue(key)
        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)
        
    def remove(self, key):
        hv = self.calculate_hashValue(key)

        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)
    
    def contains(self, key):
        hv = self.calculate_hashValue(key)

        if self.table[hv] != None:
            return key in self.table[hv]
        return False
