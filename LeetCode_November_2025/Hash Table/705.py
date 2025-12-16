from typing import *

class MyHashSet:

    def __init__(self):
        self.set = set()

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.set:
            return True 
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(9)
obj.remove(19)
obj.add(14)
obj.remove(19)