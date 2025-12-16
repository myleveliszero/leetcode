class MinStack:

    def __init__(self):
        self.stack =  []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or val < min_val:
            min_val = val
        self.stack.append((val, min_val))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op = ["MinStack","push","push","getMin","getMin","push",
      "getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]

input = [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]

test(op, input)