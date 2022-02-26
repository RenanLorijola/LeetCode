class MyHashSet:
    def __init__(self):
        self.set=set()
        
    def add(self, key):
        self.set.add(key)

    def contains(self, key):
        return key in self.set

    def remove(self, key):
        if self.contains(key):
            self.set.remove(key)

myHashSet = MyHashSet()
print(myHashSet.add(1))      # set = [1]
print(myHashSet.add(2))      # set = [1, 2]
print(myHashSet.contains(1)) # return True
print(myHashSet.contains(3)) # return False, (not found)
print(myHashSet.add(2))      # set = [1, 2]
print(myHashSet.contains(2)) # return True
print(myHashSet.remove(2))   # set = [1]
print(myHashSet.contains(2)) # return False, (already removed)