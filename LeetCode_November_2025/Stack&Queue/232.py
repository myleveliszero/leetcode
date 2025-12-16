class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def head(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    
    def tail(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def push(self, x: int) -> None:
        self.tail()
        self.stack1.append(x)

    def pop(self) -> int:
        self.head()
        return self.stack2.pop()

    def peek(self) -> int:
        self.head()
        return self.stack2[-1]

    def empty(self) -> bool:
        self.tail()
        return not self.stack1

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op = ["MyQueue", "push", "push", "peek", "pop", "empty"]

input = [[], [1], [2], [], [], []]

test(op, input)