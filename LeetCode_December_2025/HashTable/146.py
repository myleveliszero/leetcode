
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = dict()
#         self.count = 0

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.count += 1
#             val, _ = self.cache.pop(key)
#             self.cache[key] = [val, self.count]
#             return val
#         return -1

#     # def remove(self):
#     #     key_name, min_val = 0, self.capacity+1
#     #     for key in self.cache.keys():
#     #         _, count = self.cache[key]

#     def put(self, key: int, value: int) -> None: 
#         self.count += 1
#         if len(self.cache) < self.capacity:
#             if key in self.cache:
#                 _, _ = self.cache.pop(key)
#                 self.cache[key] = [value, self.count]
#             else:
#                 self.cache[key] = [value, self.count]
#         else:
#             pass
            


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

# def test(op, input):
#     obj = eval(f"{op[0]}({input[0][0]},{input[0][1]})")
#     for i in range(1, len(input)):
#         # if not input[i]:
#         #     print(eval(f"obj.{op[i]}()"))
#         if len(input[i]) == 2:
#             print(eval(f"obj.{op[i]}({input[i][0]}, {input[i][1]})"))
#         else:
#             print(eval(f"obj.{op[i]}({input[i][0]})"))

# # op = ["KthLargest", "add", "add", "add", "add", "add"]
# op = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# input = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# # input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# test(op, input)