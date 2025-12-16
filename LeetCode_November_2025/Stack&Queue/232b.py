class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.front = self.stack1[0]

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False
    

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op = ["MyQueue", "push", "push", "push", "push", "peek", "pop", "empty", "pop", "push", "pop", "pop", "peek","pop","empty"]

input = [[], [1], [2],[9],[11], [], [], [], [], [99], [],[],[],[],[]]

test(op, input)