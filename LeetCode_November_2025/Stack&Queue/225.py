import collections
class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return False if self.q1 else True
        

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()")) 
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op =["MyStack", "push", "push", "top", "pop", "empty"]
input = [[], [1], [2], [], [], []]

# input = [[], [1], [3], [-1, 50], [1], [1], [1]]

test(op, input)