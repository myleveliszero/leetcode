from typing import List
import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mheap = nums.copy()
        hq.heapify(self.mheap)
        while len(self.mheap) > k:
            hq.heappop(self.mheap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.mheap) == self.k:
            if self.mheap[0] < val:
                hq.heappushpop(self.mheap, val)
        else:
            hq.heappush(self.mheap, val)
        
        return self.mheap[0]
        
def test(op, input):
    obj = eval(f"{op[0]}({input[0][0]},{input[0][1]})")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        # else:
        print(eval(f"obj.{op[i]}({input[i][0]})"))

# op = ["KthLargest", "add", "add", "add", "add", "add"]
op = ["KthLargest","add","add","add","add","add"]
input = [[2,[0]],[-1],[1],[-2],[-4],[3]]

# input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

test(op, input)