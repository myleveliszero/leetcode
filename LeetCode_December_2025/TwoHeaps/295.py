import heapq as hq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if not (self.small or self.large):
            hq.heappush(self.small, -num)
            return
        if not self.large:
            hq.heappush(self.large, num)
            return 

        hq.heappush(self.small, -num)

        if -self.small[0] > self.large[0]:
            small = hq.heappop(self.small)
            large = hq.heappop(self.large)
            hq.heappush(self.large, -small)
            hq.heappush(self.small, -large)
        
        if len(self.small) - len(self.large) > 1:
            val = hq.heappop(self.small)
            hq.heappush(self.large, -val)
        if len(self.large) - len(self.small) > 1:
            val = hq.heappop(self.large)
            hq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-self.small[0]+self.large[0]) / 2
        



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "addNum", "findMedian"]

inp = [[], [4], [7], [], [3], [], [5], [1], []]

import random as r

def test_algo():
    obj = MedianFinder()
    op = ["MedianFinder"]
    inp = [[]]
    val = []
    i = r.randrange(1, 10)
    for _ in range(i):
        num = r.randrange(-100, 100)
        obj.addNum(num)
        inp.append([num])
        op.append("addNum")
        find_median = r.choice([True, False])
        if find_median:
            val.append(obj.findMedian())
            op.append("findMedian")
            inp.append([])
    
    return (op, inp, val)

for _ in range(10):
    op, inp, val = test_algo()
    print("------------")
    print(f"{op}".replace('\'', '\"'))
    print(inp)
    print(val)
