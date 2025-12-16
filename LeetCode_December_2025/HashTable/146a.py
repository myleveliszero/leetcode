class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None: 
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.pop(next(iter(self.cache)))
                self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def test(op, input):
    obj = eval(f"{op[0]}({input[0][0]})")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        if len(input[i]) == 2:
            print(eval(f"obj.{op[i]}({input[i][0]}, {input[i][1]})"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

# op = ["KthLargest", "add", "add", "add", "add", "add"]
op = ["LRUCache","get","put","get","put","put","get","get"]
input = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

# input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

test(op, input)