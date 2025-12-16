class BrowserHistory:
    class ListNode:
        def __init__(self, val, prev=None, next=None):
            self.val = val 
            self.next = next
            self.prev = prev

    def __init__(self, homepage: str):
        self.node = self.ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = self.ListNode(val=url, prev=self.node, next=None)
        self.node.next = new_node
        self.node = new_node

    def back(self, steps: int) -> str:
        while steps and self.node.prev != None:
            self.node = self.node.prev
            steps -= 1

        return self.node.val

    def forward(self, steps: int) -> str:
        while steps and self.node.next != None:
            self.node = self.node.next
            steps -= 1

        return self.node.val


def test(op, input):
    str = input[0][0]
    print(f'{op[0]}("{str})"')
    obj = eval(f'{op[0]}("{str}")')
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            if isinstance(input[i][0], int): 
                print(eval(f'obj.{op[i]}({input[i][0]})'))
            else:
                print(eval(f'obj.{op[i]}("{input[i][0]}")'))


op = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]     
input = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]


test(op, input)
