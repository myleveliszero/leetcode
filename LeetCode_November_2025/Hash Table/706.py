class MyHashMap:

    def __init__(self):
        # y = x % a
        self.a = 10**6+1
        self.keys = [0]*self.a

    def hash(self, key):
        idx = key % self.a        
        return idx

    def put(self, key: int, value: int) -> None:
        y = self.hash(key)
        if self.keys[y] == 0:
            self.keys[y] = [key, value]
        self.keys[y][1] = value
        
    def get(self, key: int) -> int:
        y = self.hash(key)
        if self.keys[y] != 0:
            return self.keys[y][1]
        return -1

    def remove(self, key: int) -> None:
        y = self.hash(key)
        if self.keys[y] != 0:
            self.keys[y] = 0
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.get(3))

print(obj.put(2,1))
print(obj.get(2))
print(obj.remove(2)) 
print(obj.get(2))