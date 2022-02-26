class Bucket:
    def __init__(self):
        self.bucket=[]
        
    def update(self, key):
        found = False
        for i, k in enumerate(self.bucket):
            if k == key:
                found = True
                self.bucket[i] = key
                break
        if not found:
            self.bucket.append(key)

    def get(self, key):
        for k in self.bucket:
            if k == key:
                return True
        return False

    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if k == key:
                self.bucket.pop(i)


class MyHashSet:
    def __init__(self):
        self.key_space = 2096
        self.hash_table=[Bucket() for i in range(self.key_space)]
    
    def generateHashKey(self, key):
        return key%self.key_space

    def add(self, key: int) -> None:    
        self.hash_table[self.generateHashKey(key)].update(key)
        
    def remove(self, key: int) -> None:
        self.hash_table[self.generateHashKey(key)].remove(key)
        
    def contains(self, key: int) -> bool:
        return self.hash_table[self.generateHashKey(key)].get(key)

myHashSet = MyHashSet()
print(myHashSet.add(1))      # set = [1]
print(myHashSet.add(2))      # set = [1, 2]
print(myHashSet.contains(1)) # return True
print(myHashSet.contains(3)) # return False, (not found)
print(myHashSet.add(2))      # set = [1, 2]
print(myHashSet.contains(2)) # return True
print(myHashSet.remove(2))   # set = [1]
print(myHashSet.contains(2)) # return False, (already removed)